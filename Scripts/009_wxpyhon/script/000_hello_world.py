#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Le 'hello world' de WxPython

Une application wx de base.
"""
import wx

class Bonjour(wx.Frame):
    """
    Fenêtre où on affichera le message 'Bonjour tout le monde !'
    """
    def __init__(self, titre):
        # Appel du constructeur parent
        super().__init__(None, title=titre, size=(200, 100))

        # A panel est une fenêtre sur laquelle on place des contrôles
        # de la taille de son parent
        panel = wx.Panel(self, size=self.GetClientSize())

        # Texte statique centré
        text = wx.StaticText(panel, label="Bonjour tout le monde !")
        text.Centre()

class HelloWorldApp(wx.App):
    def OnInit(self):
        # Creation de la fenêtre
        fen = Bonjour("Titre de ma fenêtre")

        # Affichage
        fen.Show()

        # Retourne Vrai pour signaler que tout s'est bien passé
        return True

if __name__ == '__main__':
    # On construit notre application
    app = HelloWorldApp()

    # Boucle infinie de l'application
    app.MainLoop()
