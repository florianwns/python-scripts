#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kivy et Pyo
"""
import kivy
kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.boxlayout import BoxLayout
import kivy.core.window
from functools import partial
from pyo import *

numSinus = 10

class SinePlayer(App):
    def __init__(self):
        super(SinePlayer, self).__init__()
        self.server = Server().boot()
        self.server.start()
        self.freqs = [x * 100 + 100 for x in range(numSinus)]
        self.amps = [0 for x in range(numSinus)]
        self.sine = Sine(freq = self.freqs, mul = self.amps).out()
        self.sliders = []

    def slider_callback(self, instance, value, **kwargs):
        self.amps[kwargs["id"]] = value
        self.sine.mul = [1. / numSinus * x for x in self.amps]

    def build(self):
        SCREEN_WIDTH = kivy.core.window.Window.size[0]
        SCREEN_HEIGHT = kivy.core.window.Window.size[1]
        layout = BoxLayout()
        layout.size = [SCREEN_WIDTH, SCREEN_HEIGHT * 0.8]
        layout.pos = [SCREEN_WIDTH / 2 - layout.width / 2, SCREEN_HEIGHT / 2 - layout.height / 2]
        for sinus in range(numSinus):
            self.sliders.append(Slider(min = 0., max = 1., orientation = 'vertical', size_hint=(1, .8)))
            self.sliders[sinus].bind(value = partial(self.slider_callback, id = sinus))
            layout.add_widget(self.sliders[sinus])
        return layout

    def on_stop(self):
        self.server.stop()

if __name__ == '__main__':
    sinePlayer =  SinePlayer()
    try:
        sinePlayer.run()
    except KeyboardInterrupt:
        sinePlayer.stop()
