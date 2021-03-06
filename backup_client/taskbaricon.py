#!/usr/bin/env python
import wx.adv
class TaskBarIcon(wx.adv.TaskBarIcon):
    def __init__(self, frame, icon, iconType=wx.adv.TBI_DEFAULT_TYPE):
        wx.adv.TaskBarIcon.__init__(self)
        self.frame = frame
        bmp = wx.Bitmap(wx.Image(icon))
        self.icon = wx.Icon(bmp)
        self.SetIcon(self.icon, "Restore")

        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.on_left_click)

    def OnTaskBarClose(self, evt):
        self.frame.Close()

    def on_left_click(self, event):
        self.frame.Show()
        self.frame.Restore()
