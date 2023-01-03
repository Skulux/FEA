import home
import wx


class home(home.frame_main):
    def __init__(self, parent):
        super().__init__(parent)
        self.Show()

if __name__ == "__main__":
    app = wx.App()
    frame = home(None)
    app.MainLoop()
