#! /usr/bin/python3
"""
    docstring here
"""
import tkinter
from LoginWindow import LoginWindow
from MainWindow import MainWindow, save_obj,load_obj
from backup_client.filehandler import observer


def main():
    try:
        credentials = load_obj("udata")
    except FileNotFoundError:
        login = tkinter.Tk()
        dialog = LoginWindow(login)
        login.wait_window()
        credentials = dialog.result
    if credentials is not None:
        myobserver = observer.FileObserver(credentials[0], credentials[1])
        myobserver.start()

        top = tkinter.Tk()
        top.geometry("250x350")
        top.title("gibc")
        main_window = MainWindow(top, myobserver)
        top.mainloop()
        save_obj(myobserver.patterns, "patterns")
        myobserver.stop()


if __name__ == "__main__":
    main()
#Hyfsat bra doc
#http://effbot.org/tkinterbook/wm.htm
#Värdelös men vill ha ändå https://www.tutorialspoint.com/python/python_gui_programming.htm
