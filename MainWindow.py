"""
    docstring here
"""
import tkinter
from tkinter import filedialog
import pickle
import os


def save_obj(obj, name):
    with open('obj/'+ name + '.pkl', 'wb') as file:
        pickle.dump(obj, file, pickle.HIGHEST_PROTOCOL)

def load_obj(name):
    with open('obj/' + name + '.pkl', 'rb') as file:
        return pickle.load(file)

class MainWindow(tkinter.Frame):
    """Gui Class

    Arguments:
        tkinter {Frame} --
    """

    def __init__(self, parent, observer, *args, **kwargs):
        """Gui for app

        Arguments:
            tkinter {Frame} -- asd
            parent {Frame} -- Root Window
            observer {Observer} -- Fileobserver to handle files.
        """

        tkinter.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.observer = observer
        # Creating menu
        menu = tkinter.Menu(parent)
        parent.config(menu=menu)

        file_menu = tkinter.Menu(menu)
        file_menu.add_command(label="Add Folder", command=self.add_folder)
        file_menu.add_command(label="Add File", command=self.add_file)

        menu.add_cascade(label="File", menu=file_menu)

        self.parent.grid_columnconfigure(2, weight=1)
        self.parent.grid_rowconfigure(0, weight=1)
        # --------------------------------------------------------------------------------------

        # Creating and adding scrollbars to monitored_files list.
        self.monitored_files = tkinter.Listbox(
            self.parent, exportselection=0, width=30)
        self.monitored_files.bind('<<ListboxSelect>>', self.on_selected_dir)
        self.monitored_files.grid(row=0, column=0, sticky="ns")

        mf_yscroll = tkinter.Scrollbar(self.parent)
        mf_yscroll.grid(row=0, column=1, sticky="ns")
        mf_yscroll.config(command=self.monitored_files.yview)
        mf_xscroll = tkinter.Scrollbar(self.parent)
        mf_xscroll.grid(row=1, column=0, sticky="we")
        mf_xscroll.config(
            command=self.monitored_files.xview, orient=tkinter.HORIZONTAL)

        self.monitored_files.config(
            yscrollcommand=mf_yscroll.set, xscrollcommand=mf_xscroll.set)
        # --------------------------------------------------------------------------------------

        current_directory = tkinter.Listbox(parent, exportselection=0)
        current_directory.grid(
            row=0, column=2, rowspan=2, sticky="nswe", padx=1, pady=1)
        self.load_stored_patterns()
    def add_file(self):
        """Add File function
        """

        file_path = tkinter.filedialog.askopenfilename()
        if isinstance(file_path, str) and file_path not in self.observer.patterns.values():
            self.observer.add_file(file_path)
            self.monitored_files.insert(tkinter.END, file_path)

    def add_folder(self):
        """Add Folder function
        """
        dir_path = filedialog.askdirectory()
        if not os.path.isdir(dir_path):
            return

        if isinstance(dir_path, str) and dir_path not in self.observer.patterns.values():
            self.observer.add_dir(dir_path)
            self.monitored_files.insert(tkinter.END, dir_path)
    def load_stored_patterns(self):
        try:
            self.observer.patterns = load_obj("patterns")
            for obj in self.observer.patterns.keys():
                self.observer.file_observer.schedule(self.observer.event_handler, obj)
                self.monitored_files.insert(tkinter.END, obj)

        except FileNotFoundError:
            pass
        except BaseException as error:
            print("Unexpected error:", error)

    def on_selected_dir(self, event):
        """Function to redraw current_window when changing monitored_files list item.

        Arguments:
            event {Virtualevent} -- Event containing Listobject
        """
        pass
        #This is retarded but who a I to judge
        #path = event.widget.get(event.widget.curselection()[0])
        #Do stuff to current_dir window


# Hides window to the user and redraws it after 5 sec.
#self.parent.wm_state("withdrawn")
#time.sleep(5)
#self.parent.wm_state("normal")
#https://www.daniweb.com/programming/software-development/threads/291184/python-tkinter-how-to-popup-from-system-tray
#http://effbot.org/tkinterbook/wm.htm#wm.Wm.withdraw-method
