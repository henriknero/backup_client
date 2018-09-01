#! /usr/bin/python3
#coding=utf-8
"""
    docstring here
"""
import tkinter
from backup_client.frames import Loginwindow, Mainwindow, load_obj


def main():
    try:
        credentials = load_obj("udata")
    except FileNotFoundError:
        login = tkinter.Tk()
        dialog = Loginwindow(login)
        login.wait_window()
        credentials = dialog.result

    if credentials is not None:
        top = tkinter.Tk()
        top.geometry("250x350")
        top.title("Git Backup Client")
        Mainwindow(top, credentials)
        top.mainloop()


if __name__ == "__main__":
    main()
#Hyfsat bra doc
#http://effbot.org/tkinterbook/wm.htm
#Värdelös men vill ha ändå https://www.tutorialspoint.com/python/python_gui_programming.htm