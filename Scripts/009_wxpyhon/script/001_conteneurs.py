#!/usr/bin/env python
# encoding: utf-8
"""
Introduction à WxPython

Les conteneurs délimitent l'espace où les objets
graphiques seront affichés.
"""
import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title, pos, size):
        super().__init__(parent, title=title, pos=pos, size=size)
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour("#DDFFDD")

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None, title='Simple App', pos=(20, 20), size=(250, 200))
    frame.Show()
    app.MainLoop()
