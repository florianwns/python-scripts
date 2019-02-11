#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""PyAudio

Ressources :
 - https://www.programcreek.com/python/example/52624/pyaudio.PyAudio
 - https://people.csail.mit.edu/hubert/pyaudio/docs/#module-pyaudio

Installation on Mac OS

xcode-select --install
brew remove portaudio
brew install portaudio
pip3 install pyaudio

"""
import math        # import needed modules
import pyaudio     # sudo apt-get install python-pyaudio

PyAudio = pyaudio.PyAudio     #initialize pyaudio

BITRATE = 16000     # number of frames per second/frameset.
FREQUENCY = 500     # Hz, waves per second, 261.63=C4-note.
LENGTH = 1          # seconds to play sound

if FREQUENCY > BITRATE:
    BITRATE = FREQUENCY+100

NUMBEROFFRAMES = int(BITRATE * LENGTH)
RESTFRAMES = NUMBEROFFRAMES % BITRATE
WAVEDATA = ''

# Generating wawes
for x in range(NUMBEROFFRAMES):
    WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))

for x in range(RESTFRAMES):
    WAVEDATA = WAVEDATA+chr(128)

p = PyAudio()
stream = p.open(format = p.get_format_from_width(1),
                channels = 1,
                rate = BITRATE,
                output = True)

stream.write(WAVEDATA)
stream.stop_stream()
stream.close()
p.terminate()
