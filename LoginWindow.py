"""LoginWindow module
"""

import tkinter as tk
from tkinter import ttk
import requests
from MainWindow import save_obj


class LoginWindow(object):
    """Gui Class

    Arguments:
        tkinter {Frame} --
    """

    def __init__(self, parent):
        self.result = None
        self.parent = parent
        self.parent.bind('<Return>', self.apply)
        self.store_password = tk.IntVar()

        #Creating and configuring Widgets
        username_label = ttk.Label(self.parent, text="Username")
        self.username_entry = ttk.Entry(self.parent)
        password_label = ttk.Label(self.parent, text="Password")
        self.password_entry = ttk.Entry(self.parent)
        self.password_entry.config(show="*")
        self.pw_checkbox = ttk.Checkbutton(self.parent,
                                           text="Always login as this user",
                                           variable=self.store_password
                                          )
        login = ttk.Button(parent, text="Login", command=self.apply)

        #Packing widgets
        username_label.pack()
        self.username_entry.pack(padx=4, pady=5)
        password_label.pack()
        self.password_entry.pack(padx=4, pady=5)
        self.pw_checkbox.pack()
        login.pack(pady=5)

    def apply(self, optional = None):
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
