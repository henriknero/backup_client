"""Frames Module
"""
import tkinter
from tkinter import filedialog, simpledialog, messagebox
import os
import logging

import requests as req
import config
from backup_client.network import get_reponame_from_path, is_repo, remove_local_repo_data
from backup_client import Backend
from backup_client.network.gogs import GitApi
from backup_client.filehandler.pickles import load_obj, save_obj

logger = logging.getLogger(__name__)


class Loginwindow(object):
    def __init__(self, parent):
        self.result = None
        self.parent = parent
        self.parent.bind('<Return>', self.apply)
        self.store_password = tkinter.IntVar()

        #Creating and configuring Widgets
        username_label = tkinter.Label(self.parent, text="Username")
        self.username_entry = tkinter.Entry(self.parent)
        password_label = tkinter.Label(self.parent, text="Password")
        self.password_entry = tkinter.Entry(self.parent)
        self.password_entry.config(show="*")
        self.pw_checkbox = tkinter.Checkbutton(self.parent,
                                               text="Always login as this user",
                                               variable=self.store_password
                                               )
        login = tkinter.Button(parent, text="Login", command=self.apply)

        #Packing widgets
        username_label.pack()
        self.username_entry.pack(padx=4, pady=5)
        password_label.pack()
        self.password_entry.pack(padx=4, pady=5)
        self.pw_checkbox.pack()
        login.pack(pady=5)

    def apply(self, optional=None):
        """Check against server
        """
        self.result = (self.username_entry.get(), self.password_entry.get())
        if GitApi(config.API, self.result).is_authorized():
            if self.store_password.get():
                save_obj(self.result, "udata")
            self.parent.destroy()


class Mainwindow(tkinter.Frame):
    """Gui Class

    Arguments:
        tkinter {Frame} --
    """

    def __init__(self, parent, gitgogs, *args, **kwargs):
        tkinter.Frame.__init__(self, parent, *args, **kwargs)
        self.gitgogs = gitgogs
        self.parent = parent
        self.parent.protocol("WM_DELETE_WINDOW", self.quit)

        self.create_menu()
        self.create_monitored_folders_box()

        self.load_stored_patterns()

        self.parent.grid_columnconfigure(0, weight=1)
        self.parent.grid_rowconfigure(0, weight=1)

    def quit(self):
        self.gitgogs.stop()
        save_obj(self.gitgogs.patterns, "patterns")
        self.parent.destroy()

    def add_folder(self, askdir=os.getcwd()):
        """Add Folder function
        """
        dir_path = filedialog.askdirectory(initialdir=askdir)
        if isinstance(dir_path, str) and dir_path != '':
            git_name = simpledialog.askstring(
                "Alias for folder",
                "Enter the name you want for the git repo and what you will see"
                )
        if not os.path.isdir(dir_path):
            return

        self.gitgogs.add_dir(dir_path, git_name)
        self.monitored_files.insert(tkinter.END, git_name)

    def load_stored_patterns(self):
        try:
            temp = load_obj("patterns")
            logger.info("Patterns: Loading") if temp else logger.info("No Patterns to Load")
            for obj in temp:
                reponame = get_reponame_from_path(obj)
                if reponame is None:
                    answer = messagebox.askyesno("Repository not found", "Local repository in {} does not exist, do you want to create it?".format(obj))
                    if answer:
                        self.add_folder(askdir=obj)
                    else:
                        self.gitgogs.add_dir(obj, reponame)
                        self.monitored_files.insert(tkinter.END, reponame)
            if temp : logger.info("Patterns:Done Loading")
        except FileNotFoundError:
            pass

    def on_selected_dir(self, event):
        pass
        #path = event.widget.get(event.widget.curselection()[0])

    def create_menu(self):
        menu = tkinter.Menu(self.parent)
        self.parent.config(menu=menu)

        file_menu = tkinter.Menu(menu)
        file_menu.add_command(label="Add Folder", command=self.add_folder)
        file_menu.add_command(label="Connect to existing Remote", command=self.connect_remote)
        file_menu.add_separator()
        file_menu.add_command(label="Logout and Quit", command=self.logout)
        file_menu.add_command(label="Quit", command=self.quit)

        menu.add_cascade(label="File", menu=file_menu)

    def create_monitored_folders_box(self):
        self.monitored_files = tkinter.Listbox(
            self.parent,
            exportselection=0
            )
        self.monitored_files.bind('<<ListboxSelect>>', self.on_selected_dir)
        self.monitored_files.grid(row=0, column=0, sticky="nswe")
        mf_yscroll = tkinter.Scrollbar(self.parent)
        mf_yscroll.grid(row=0, column=1, sticky="ns")
        mf_yscroll.config(
            command=self.monitored_files.yview
            )
        mf_xscroll = tkinter.Scrollbar(self.parent)
        mf_xscroll.grid(row=1, column=0, sticky="we")
        mf_xscroll.config(
            command=self.monitored_files.xview,
            orient=tkinter.HORIZONTAL
            )
        self.monitored_files.config(
            yscrollcommand=mf_yscroll.set,
            xscrollcommand=mf_xscroll.set
            )

        self.monitored_files.bind("<Button-3>", self.mf_menu_popup)
        self.mf_menu = tkinter.Menu(self.parent)
        self.mf_menu.add_command(label="Remove from Remote", command=self.remove_folder_git)

    def mf_menu_popup(self, event):
        event.widget.selection_clear(0, tkinter.END)
        event.widget.select_set(event.widget.nearest(event.y))
        event.widget.activate(event.widget.nearest(event.y))
        try:
            self.mf_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.mf_menu.grab_release()

    def remove_folder_git(self):
        repo_name = self.monitored_files.get(self.monitored_files.curselection())
        try:
            self.gitgogs.remove_dir(repo_name)
            self.monitored_files.delete(self.monitored_files.curselection())
        except NameError:
            logger.warning(" Repository {} was not found on remote server".format(repo_name)) # Create option to remove .git folder and clean up cause remote repository doesnt exist

    def connect_remote(self):
        dir_path = filedialog.askdirectory(title="Folder to download repository too")
        if not is_repo(dir_path): # If local repository does not exist download repository to folder
            repo_name = simpledialog.askstring(
                "Add Remote Folder",
                "The folder you have entered does not contain any remote, please enter the name of remote folder"
                )
            add_remote_repo(dir_path, repo_name, self.observer.credentials)
            self.observer.add_dir(dir_path, repo_name)
            self.monitored_files.insert(tkinter.END, repo_name)
        else: # If choosen folder is existing repository, try to pull it to update local repository
            repo_name = get_reponame_from_path(dir_path)
            pull(find_repo(dir_path), self.observer.credentials, get_signature(self.observer.credentials))
            self.observer.add_dir(dir_path, repo_name)
            self.monitored_files.insert(tkinter.END, repo_name)

    def logout(self):
        os.remove('obj/udata.pkl')
        self.quit()

# Hides window to the user and redraws it after 5 sec.
#self.parent.wm_state("withdrawn")
#time.sleep(5)
#self.parent.wm_state("normal")
#https://www.daniweb.com/programming/software-development/threads/291184/python-tkinter-how-to-popup-from-system-tray
#http://effbot.org/tkinterbook/wm.htm#wm.Wm.withdraw-method



 #En ide...
        # self.canvas = tkinter.Canvas(self.parent)
        # self.frame = tkinter.Frame(self.canvas)
        # h = tkinter.Scrollbar(self.parent, orient=tkinter.HORIZONTAL, command=self.canvas.xview)
        # v = tkinter.Scrollbar(self.parent, orient=tkinter.VERTICAL, command=self.canvas.yview)
        # self.canvas.config(yscrollcommand=v.set, xscrollcommand=h.set,width=250)

        # self.canvas.grid(column=0, row=0, sticky="nwes")
        # h.grid(column=0, row=1, sticky="we")
        # v.grid(column=1, row=0, sticky="ns")
        # self.canvas.create_window((0,0),window=self.frame,anchor='nw')
        # self.frame.bind("<Configure>",self.scrollevent)

        # for row in range(100):
        #     ListItem(self.frame, "%s" % row, "testing").grid(row=row, column=0)
        #     t="this is the second column for row %s" %row
        #     label = ListItem(self.frame, t, "asdasdasd")
        #     label.grid(row=row, column=1)
        #     label.bind('<Button-1>',self.self)
