import wx
import os
from OptionsPane import *

class MainWindow(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title,size=(800,800))

if __name__ == '__main__':
    app = wx.App(False)
    frame = MainWindow(None, title = "CommTester")
    panel = OptionsPane(frame)
    frame.Show()
    app.MainLoop()
