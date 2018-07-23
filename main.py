#! /usr/bin/python3
"""
    docstring here
"""
import tkinter
from LoginWindow import LoginWindow
from MainWindow import MainWindow, save_obj
from backup_client.filehandler import observer


def main():
    login = tkinter.Tk()
    dialog = LoginWindow(login)
    login.wait_window()
    if dialog.result is not None:
        myobserver = observer.FileObserver(dialog.result[0],dialog.result[1])
        myobserver.start()

        top = tkinter.Tk()
        top.geometry("800x500")
        MainWindow(top, myobserver)
        top.mainloop()
        save_obj(myobserver.patterns, "patterns")
        myobserver.stop()


if __name__ == "__main__":
    main()
#Hyfsat bra doc
#http://effbot.org/tkinterbook/wm.htm
#Värdelös men vill ha ändå https://www.tutorialspoint.com/python/python_gui_programming.htm
