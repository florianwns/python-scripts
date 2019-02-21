#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Camera Example
==============

Cet exemple montre l'utilisation de la webcam. Cela affiche une fenêtre avec
un boutton "afficher" pour mettre en marche la caméra et l'éteindre.
Il se peut que la webcam ne fonctionne pas si gstreamer n'est pas installé, ce
qui va jeté une exception pendant le traitement du langage kv.

Source : https://kivy.org/doc/stable/examples/gen__camera__main__py.html
"""

# Décommenter ces lignes afin de voir les messages de débug
#from kivy.logger import Logger
#import logging
#Logger.setLevel(logging.TRACE)

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import time
Builder.load_string("""
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640, 480)
        play: False
    ToggleButton:
        text: 'Play'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
""")

class CameraClick(BoxLayout):
    def capture(self):
        """
        Fonction qui capture les images et leur donne un nom en fonction
        de l'heure et de la date où la capture a été prise.
        """
        camera = self.ids['camera']
        filename = "IMG_{}.png".format(time.strftime("%Y%m%d_%H%M%S"))
        camera.export_to_png(filename)
        print("Capture :", filename)

class TestCamera(App):
    def build(self):
        return CameraClick()

if __name__ == '__main__':
    TestCamera().run()
