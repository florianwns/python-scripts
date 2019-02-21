#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Faire du bruit avec Numpy
"""
from pyo import *
import numpy as np

s = Server().boot()

# récupère la taille du buffer
bs = s.getBufferSize()

# Crée une table de la longueur du buffer et la lit en boucle
t = DataTable(size=bs)
osc = TableRead(t, freq=t.getRate(), loop=True, mul=0.1).out()

# Partage la mémoire du tableau avec le numpy array
arr = np.asarray(t.getBuffer())

def white_noise():
    "Remplit le tableau (donc la table t) avec du bruit blanc"
    arr[:] = np.random.normal(0.0, 0.5, size=bs)

# Appel la fonction 'white_noise' au début de chaque boucle de traitement.
s.setCallback(white_noise)

# Démarre le serveur
s.start()

s.gui(locals())
