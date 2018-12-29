import wx
import config

class TaskBarIcon(wx.adv.TaskBarIcon):
    def __init__(self, frame, iconType=wx.adv.TBI_DEFAULT_TYPE):
        wx.adv.TaskBarIcon.__init__(self)
        self.frame = frame
        try:
            bmp = wx.Bitmap(wx.Image('icon.png'))
        except:
            bmp = wx.Bitmap(config.ICON)
        self.icon = wx.Icon(bmp)
        self.SetIcon(self.icon,"Restore")

        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.on_left_click)

    def OnTaskBarActivate(self, evt):
        """"""
        pass
    
    def OnTaskBarClose(self, evt):
        """
        Destroy the taskbar icon and frame from the taskbar icon itself
        """
        self.frame.Close()
    def on_left_click(self, event):
        self.frame.Show()
        self.frame.Restore()