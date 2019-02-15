#!/usr/bin/env python
# encoding: utf-8
"""
Le 'hello world' de WxPython

Une application wx minimale. Le passage du contrôle
de la boucle d'exécution à WxPython.
"""
import wx

# Crée une nouvelle fenêtre
# False pour ne pas rediriger stdout/stderr vers une fenêtre
app = wx.App(False)
# Un cadre est une fenêtre de niveau supérieur
frame = wx.Frame(None, wx.ID_ANY, "Hello World")

# Affiche le cadre
frame.Show(True)
app.MainLoop()
