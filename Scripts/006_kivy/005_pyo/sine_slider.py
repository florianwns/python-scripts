#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kivy et Pyo
"""
from kivy.app import App
from kivy.uix.slider import Slider
from pyo import *

class AudioApp(App):
    def build(self):
        super(AudioApp, self).__init__()
        self.server = Server().boot().start()
        self.slider = Slider(min=110, max=880, value=440)
        self.slider.bind(value=self.update_freq)
        self.sine = Sine(440, mul = 0.1).out()
        return self.slider

    def update_freq(self, slider, value):
        self.sine.setFreq(value)

    def on_stop(self):
        self.server.stop()

if __name__ == '__main__':
    audioApp =  AudioApp()
    try:
        audioApp.run()
    except KeyboardInterrupt:
        audioApp.stop()
