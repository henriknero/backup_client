"""Frames Module
"""
import tkinter
from tkinter import filedialog, simpledialog, messagebox
import pickle
import os

import requests

from backup_client.network.gitcom import get_reponame_from_path, is_repo, add_remote_repository, pull, find_repository, verify_remote, update_remote, remove_local_repo_data
from backup_client.filehandler import observer


def save_obj(obj, name):
    with open('obj/'+ name + '.pkl', 'wb') as file:
        pickle.dump(obj, file, pickle.HIGHEST_PROTOCOL)

def load_obj(name):
    with open('obj/' + name + '.pkl', 'rb') as file:
        return pickle.load(file)

class Loginwindow(object):
    """Gui Class

    Arguments:
        tkinter {Frame} --
    """

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
        credentials = (self.username_entry.get(), self.password_entry.get())
        response = requests.get(
            'https://www.nerobp.xyz/gogs/user/login', auth=credentials)
        if response.url == 'https://www.nerobp.xyz/gogs/':
            self.result = (self.username_entry.get(),
                           self.password_entry.get())
            if self.store_password.get():
                save_obj(credentials, 'udata')
            self.parent.destroy()


class Mainwindow(tkinter.Frame):
    """Gui Class

    Arguments:
        tkinter {Frame} --
    """

    def __init__(self, parent, credentials, *args, **kwargs):
        """Gui for app

        Arguments:
            tkinter {Frame} -- asd
            parent {Frame} -- Root Window
            observer {Observer} -- Fileobserver to handle files.
        """
        tkinter.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.parent.protocol("WM_DELETE_WINDOW", self.quit)
        self.observer = observer.FileObserver(credentials[0], credentials[1])
        self.observer.start()
        self.listitems = {}

        self.create_menu()
        self.create_monitored_folders_box()

        #Reloads stored patterns into the GUI
        self.load_stored_patterns()

        #Setting weights for grid, makes stuff look good, dont know how it works...
        self.parent.grid_columnconfigure(0, weight=1)
        self.parent.grid_rowconfigure(0, weight=1)

    def quit(self):
        self.parent.destroy()
        save_obj(self.observer.patterns, "patterns")
        self.observer.stop()

    def add_folder(self, askdir=os.getcwd()):
        """Add Folder function
        """
        dir_path = filedialog.askdirectory(initialdir=askdir)
        if isinstance(dir_path, str) and dir_path != '':
            git_name = simpledialog.askstring(
                "Alias for folder",
                "Enter the name you want for the git repo and what you will see"
                )
            self.listitems[git_name] = dir_path
        if not os.path.isdir(dir_path):
            return

        if isinstance(dir_path, str) and dir_path not in self.observer.patterns.values():
            self.observer.add_dir(dir_path, git_name)
            self.monitored_files.insert(tkinter.END, git_name)

    def load_stored_patterns(self):
        try:
            temp = load_obj("patterns")
            for obj in temp:
                reponame = get_reponame_from_path(obj)
                if reponame is None:
                    answer = messagebox.askyesno("Repository not found", "Local repository in {} does not exist, do you want to create it?".format(obj))
                    if answer:
                        self.add_folder(askdir=obj)
                        break
                    else:
                        break
                response = verify_remote(obj, reponame, self.observer.credentials)
                if 1 in response:
                    answer = messagebox.askyesno("Wrong reponame", "The name of the repository does not correlate with the remote, do you want to change it to do so?")
                    if answer:
                        reponame = get_reponame_from_path(obj)
                    else:
                        break
                if 2 in response:
                    answer = messagebox.askyesno("No remote folder found", "Do you want to change reponame?")
                    if answer:
                        reponame = simpledialog.askstring("Renaming repo", "Enter new name for repository")
                    else:
                        answer = messagebox.askyesno("Wrong Reponame", "Do you want to delete local repository data?")
                        if answer:
                            remove_local_repo_data(obj)
                update_remote(obj, self.observer.credentials)
                if reponame is not None:
                    self.observer.patterns[obj] = temp[obj]
                    self.observer.file_observer.schedule(self.observer.event_handler, obj)
                    self.monitored_files.insert(tkinter.END, reponame)
                    self.listitems[reponame] = obj


        except FileNotFoundError:
            pass

    def on_selected_dir(self, event):
        """Function to redraw current_window when changing monitored_files list item.

        Arguments:
            event {Virtualevent} -- Event containing Listobject
        """
        pass
        #path = event.widget.get(event.widget.curselection()[0])

    def create_menu(self):
        menu = tkinter.Menu(self.parent)
        self.parent.config(menu=menu)

        file_menu = tkinter.Menu(menu)
        file_menu.add_command(label="Add Folder", command=self.add_folder)
        file_menu.add_command(label="Connect to existing Remote", command=self.connect_remote)

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
            self.observer.unmonitor_folder(repo_name, self.listitems[repo_name])
            self.monitored_files.delete(self.monitored_files.curselection())
        except NameError:
            print("Repository was not found pls handle") # Create option to remove .git folder and clean up cause remote repository doesnt exist

    def connect_remote(self):
        dir_path = filedialog.askdirectory(title="Folder to download repository too")
        if not is_repo(dir_path): # If local repository does not exist download repository to folder
            repo_name = simpledialog.askstring(
                "Add Remote Folder",
                "The folder you have entered does not contain any remote, please enter the name of remote folder"
                )
            add_remote_repository(dir_path, repo_name, self.observer.credentials)
            self.observer.add_dir(dir_path, repo_name)
            self.monitored_files.insert(tkinter.END, repo_name)
        else: # If choosen folder is existing repository, try to pull it to update local repository
            repo_name = get_reponame_from_path(dir_path)
            pull(find_repository(dir_path), self.observer.credentials)
            self.observer.add_dir(dir_path, repo_name)
            self.monitored_files.insert(tkinter.END, repo_name)



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
