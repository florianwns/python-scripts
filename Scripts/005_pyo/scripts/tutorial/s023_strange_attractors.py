#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Equations différentielles ordinaires non linéaires.

Un attracteur étrange est un système de trois équations différentielles
ordinaires non linéaires. Ces équations différentielles définissent un système
dynamique à temps continu qui présente une dynamique chaotique associée aux
propriétés fractales de l'attracteur.

Il y a trois attracteurs étranges dans la bibliothèque, Rosssler, Lorenz
et ChenLee. Chacun peut émettre un signal stéréo si l’argument stereo est True.

Il est possible de créer un LFO très intéressante avec des attracteurs étranges.
La dernière partie de ce didacticiel montre l’utilisation de la sortie de Lorenz
pour contrôler la fréquence de deux oscillateurs à onde sinusoïdale.
"""
from pyo import *

s = Server().boot().start()

### Oscilloscope ###

# LFO appliqué à l'attribut 'chaos'
lfo = Sine(0.2).range(0, 1)

# Attracteur Rossler
n1 = Rossler(pitch=0.5, chaos=lfo, stereo=True)

# Attracteur Lorenz
n2 = Lorenz(pitch=0.5, chaos=lfo, stereo=True)

# Attracteur ChenLee
n3 = ChenLee(pitch=0.5, chaos=lfo, stereo=True)

# Interpolation entre les différents signaux
sel = Selector([n1, n2, n3])
sel.ctrl(title="Input interpolator (0=Rossler, 1=Lorenz, 2=ChenLee)")

# Affichage
sc = Scope(sel)
sp = Spectrum(sel)


### Audio ###

# Attracteur Lorenz avec une très basse valeur pour agir comme un LFO
freq = Lorenz(0.005, chaos=0.7, stereo=True, mul=250, add=500)
a = Sine(freq, mul=0.3).out()

s.gui(locals())
