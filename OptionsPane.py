import wx
import os

class OptionsPane(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent)
        self.eventLoglbl = wx.StaticText(self, label = "Event Logs:",pos=(200,600))

        self.eventLogger = wx.TextCtrl(self, pos=(200,625), size=(400,125), style = wx.TE_MULTILINE | wx.TE_READONLY)

        
