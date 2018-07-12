import time
import tkinter
from tkinter import filedialog
class MainWindow(tkinter.Frame):
    def __init__(self,parent, observer, *args, **kwargs):
        tkinter.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.observer = observer
        
        menu = tkinter.Menu(parent)
        parent.config(menu=menu)
        
        file_menu = tkinter.Menu(menu)
        file_menu.add_command(label="Add Folder", command=self.add_folder)
        file_menu.add_command(label="Add File", command=self.add_file)

        menu.add_cascade(label="File" ,menu=file_menu)
        
        self.parent.grid_columnconfigure(2,weight=1)
        self.parent.grid_rowconfigure(0,weight=1)
        
        self.monitored_files = tkinter.Listbox(self.parent, exportselection=0,width=30)
        self.monitored_files.bind('<<ListboxSelect>>', self.on_selected_dir)
        self.monitored_files.grid(row=0,column=0,sticky="ns")

        mf_yscroll = tkinter.Scrollbar(self.parent)
        mf_yscroll.grid(row=0,column=1,sticky="ns")
        mf_yscroll.config(command=self.monitored_files.yview)
        mf_xscroll = tkinter.Scrollbar(self.parent)
        mf_xscroll.grid(row=1,column=0,sticky="we")
        mf_xscroll.config(command=self.monitored_files.xview,orient=tkinter.HORIZONTAL)
        
        self.monitored_files.config(yscrollcommand=mf_yscroll.set, xscrollcommand=mf_xscroll.set)

        current_directory = tkinter.Listbox(parent, exportselection=0)
        current_directory.grid(row=0,column=2,rowspan=2,sticky="nswe",padx=1,pady=1)

    def add_file(self):
        file_path = filedialog.askopenfilename()
        if isinstance(file_path,str):
            self.observer.add_file(file_path)
            self.monitored_files.insert(tkinter.END,file_path)

    def add_folder(self):
        dir_path = filedialog.askdirectory()
        if isinstance(dir_path,str):
            self.observer.add_dir(dir_path)
            self.monitored_files.insert(tkinter.END,dir_path)
    def on_selected_dir(self,event):
        #This is retarded but who a I to judge
        path = event.widget.get(event.widget.curselection()[0])
        #Do stuff to current_dir window


# Hides window to the user and redraws it after 5 sec.
#self.parent.wm_state("withdrawn")
#time.sleep(5)
#self.parent.wm_state("normal")
#https://www.daniweb.com/programming/software-development/threads/291184/python-tkinter-how-to-popup-from-system-tray
#http://effbot.org/tkinterbook/wm.htm#wm.Wm.withdraw-method