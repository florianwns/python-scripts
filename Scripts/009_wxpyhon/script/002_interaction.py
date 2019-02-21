#!/usr/bin/env python
# encoding: utf-8
"""
Introduction à WxPython

Illustration de l'interaction entre la manipulation des objets
à l'écran et les fonctionnalités du programme.
"""
import wx

class InteractionFrame(wx.Frame):
    def __init__(self, title, size):
        super().__init__(None, title=title, size=size)
        self.panel = wx.Panel(self, size=self.GetClientSize())

        choices = ["white", "red", "green", "blue", "yellow"]
        choose = wx.Choice(self.panel, choices=choices)
        choose.SetSelection(0)
        choose.Bind(wx.EVT_CHOICE, self.changeBackColour)
        choose.Center()

    def changeBackColour(self, evt):
        self.panel.SetBackgroundColour(evt.GetString())

class InteractionApp(wx.App):
    def OnInit(self):
        frame = InteractionFrame(title='Interaction', size=(250, 200))
        frame.Show()
        return True

if __name__ == '__main__':
    app = InteractionApp()
    app.MainLoop()
