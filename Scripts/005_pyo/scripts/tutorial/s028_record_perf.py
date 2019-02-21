#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enregistrer une performance sur le disque.

L'objet Serveur permet l'enregistrement de la lecture globale (c'est exactement
ce que vous entendez). Le bouton “Rec Start” de la fenêtre du serveur le fait
avec des paramètres par défaut. Il enregistrera un fichier
appelé "pyo_rec.wav" en 16 bits 44100Hz sur le bureau de l’utilisateur.

Vous pouvez contrôler l’enregistrement avec la méthode du serveur appelée
"recordOptions".

Les arguments sont les suivants:
- dur : La durée de l'enregistrement, une valeur de -1 signifie pour toujours
(recstop () doit donc être appelé par l'utilisateur).
- filename : indique l'emplacement du fichier enregistré.
- fileformat : Le format du fichier audio (voir documentation)
- sampletype : : Le type d’échantillon du fichier audio (voir documentation)

L’enregistrement peut être déclenché avec les méthodes du Serveur recstart()
et recstop(). Afin d'enregistrer plusieurs fichiers à partir d'une performance
unique, il est possible de définir le nom du fichier avec un argument
lors de l'appel à recstart().
"""
from pyo import *
import os, time

s = Server().boot().start()

# Chemin de l'enregistrement du fichier
path = os.path.join(os.path.expanduser("~"), "Desktop", "synth.wav")

# Enregistre un fichier '.wav' de 10 secondes en 24-bit.
# http://ajaxsoundstudio.com/pyodoc/api/classes/server.html?highlight=recordoptions#pyo.Server.recordOptions
s.recordOptions(dur=-1, filename=path, fileformat=0, sampletype=1)

# Crée une enveloppe d'amplitude
amp = Fader(fadein=1, fadeout=1, dur=10, mul=0.3).play()

# un simple synthé
lfo = Sine(freq=[0.15, 0.16]).range(1.25, 1.5)
fm2 = CrossFM(carrier=200, ratio=lfo, ind1=10, ind2=2, mul=amp).out()

# Commence l'enregistre, puis stoppe au boût de 10 secondes
s.recstart()
time.sleep(10)
s.recstop()
