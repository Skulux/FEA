import home
import wx
import config as cf

class home(home.frame_main):
    def __init__(self, parent):
        super().__init__(parent)
        self.Show()

if __name__ == "__main__":
    cf.setup()
    app = wx.App()
    frame = home(None)
    app.MainLoop()
