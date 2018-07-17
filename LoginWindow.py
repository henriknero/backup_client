import tkinter as tk
from tkinter import filedialog


class LoginWindow(object):
    """Gui Class

    Arguments:
        tkinter {Frame} --
    """

    def __init__(self, parent):
        self.result = None
        self.parent = parent
        username_label = tk.Label(self.parent, text="Username")
        self.username_entry = tk.Entry(self.parent)
        password_label = tk.Label(self.parent, text="Password")
        self.password_entry = tk.Entry(self.parent)
        login = tk.Button(parent, text="Login", command= self.apply)
        username_label.pack()
        self.username_entry.pack()
        password_label.pack()
        self.password_entry.pack()
        login.pack()


    def apply(self):
        """Check against server
        """
        self.result = {self.username_entry.get(), self.password_entry.get()}
        self.parent.destroy()

