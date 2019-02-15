#!/usr/bin/env python
# encoding: utf-8
from pyo import *
import sys

READY = True           # Set to True when ready for the radio
TITLE = "Hexmod"    # The title of the music
ARTIST = "J.T.Hutton (hipnofoo)"  # Your artist name
DURATION = 210          # The duration of the music in seconds
##################### These are optional #####################
GENRE = "Electronic"    # Kind of your music, if there is any
DATE = 2015             # Year of creation

####################### SERVER CREATION ######################
s = Server().boot()

##################### PROCESSING SECTION #####################

######### Hexmod ############

h = Fader(fadein=0.01, fadeout=.1, dur=DURATION, mul=1, add=0)    .play()

e = Phasor(freq=.3, phase=0, mul=200, add=0)

x = SineLoop(80+e, feedback=.3, mul=.2)

m = Randi(min=0.001, max=.9, freq=1, mul=1, add=0)

o = Delay(x, delay=m, feedback=.9, mul=1)

d = Pan(o, outs=2, pan=m, spread=.3, mul=.5*h, add=0)   .out()

#################### START THE PROCESSING ###################
s.start()
s.gui(locals())
