#! /usr/bin/python3
import tkinter
from MainWindow import MainWindow
from os import path
from backup_client.filehandler import observer

observer = observer.FileObserver()
observer.start()

top = tkinter.Tk()
top.geometry("800x500")
MainWindow(top, observer)
top.mainloop()