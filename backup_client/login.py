#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.8.3 on Fri Dec 28 16:02:58 2018
#

import wx

import config
from backup_client.network.gogs import GitApi
from backup_client.filehandler.pickles import save_obj

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.result= None
        self.verified = False
        self.SetSize((200, 250))
        self.username_form = wx.TextCtrl(self, wx.ID_ANY, "")
        self.password_form = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_PASSWORD)
        self.checkbox_2 = wx.CheckBox(self, wx.ID_ANY, "Stay logged in")
        self.login_button = wx.Button(self, wx.ID_ANY, "Login")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.apply, self.login_button)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyDialog.__set_properties
        self.SetTitle("Gibc")
        self.SetSize((200, 250))
        self.checkbox_2.SetValue(0)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyDialog.__do_layout
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        username_label = wx.StaticText(self, wx.ID_ANY, "Username", style=wx.ALIGN_CENTER)
        username_label.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, 0, "Sans"))
        sizer_2.Add(username_label, 0, wx.ALIGN_CENTER | wx.EXPAND | wx.TOP, 10)
        sizer_2.Add(self.username_form, 0, wx.ALL | wx.EXPAND, 10)
        password_label = wx.StaticText(self, wx.ID_ANY, "Password", style=wx.ALIGN_CENTER)
        password_label.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD, 0, "Sans"))
        sizer_2.Add(password_label, 0, wx.EXPAND, 0)
        sizer_2.Add(self.password_form, 0, wx.ALL | wx.EXPAND, 10)
        sizer_2.Add(self.checkbox_2, 0, wx.ALL, 5)
        sizer_2.Add(self.login_button, 0, wx.ALIGN_CENTER, 0)
        self.SetSizer(sizer_2)
        self.Layout()
        # end wxGlade

    def apply(self, event):  # wxGlade: MyDialog.<event_handler>
        self.result = (self.username_form.GetLineText(0), self.password_form.GetLineText(0))
        if GitApi(config.API, self.result).is_authorized():
            self.verified = True
            if self.checkbox_2.GetValue():
                save_obj(self.result,'udata')
            self.EndModal(0)
# end of class MyDialog

class LoginWindow(wx.App):
    def OnInit(self):
        self.Gibc = MyDialog(None, wx.ID_ANY, "")
        self.SetTopWindow(self.Gibc)
        self.Gibc.ShowModal()
        self.credentials = (self.Gibc.username_form.GetLineText(0), self.Gibc.password_form.GetLineText(0))
        self.verified = self.Gibc.verified
        self.Gibc.Destroy()
        return True
