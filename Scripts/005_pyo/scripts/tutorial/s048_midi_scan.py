#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scan des données MIDI via la méthode RawMidi() qui permet de capter les données
brutes.

Pour plsu d'infos
http://www.onicos.com/staff/iz/formats/midi-event.html
https://www.midi.org/specifications-old/item/table-2-expanded-messages-list-status-bytes
http://laurent.bedouet.free.fr/midi/messages.php
"""
from pyo import *
from datetime import datetime

MIDI_MESSAGES = ["Note off", "Note on", "Poly Aftertouch", "Control Change",
    "Program Change", "Chan Aftertouch", "Pitch Bend", "Sysex"]

PRINT_FORMAT = "{:<13}| {:<16}| {:<8}| {:<8}"

def midi_scan(status, data1, data2):
    # Index des messages : ex : Note On => 1001 0000 >> 4 = 1001 & 0111 = 0001
    type = status >> 4 & 7
    channel = 1 + status % 16
    now = str(datetime.now().time())[:12]
    data = " ".join(map(str, [status, data1, data2]))
    print(PRINT_FORMAT.format(now, MIDI_MESSAGES[type], channel, data))

if __name__ == '__main__':
    s = Server()
    s.setMidiInputDevice(0)
    s.boot().start()
    print(PRINT_FORMAT.format("Time", "Message", "Channel", "Data"))
    a = RawMidi(midi_scan)
    s.gui(locals())
