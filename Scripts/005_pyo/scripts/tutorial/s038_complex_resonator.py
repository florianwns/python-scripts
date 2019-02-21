#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filtrage au moyen d'une multiplication complexe.

ComplexRes implémente un résonateur dérivé d'une multiplication complexe,
très similaire à un filtre numérique.

Il est utilisé ici pour créer un carillon rythmique de résonance variable.
"""
from pyo import *
import random

s = Server().boot().start()

# 6 fréquences aléatoires
freqs = [random.uniform(1000, 3000) for i in range(6)]

# 6 vitesses de déclencheurs
pluck = Metro([.9,.8,.6,.4,.3,.2]).play()

# LFO appliqué au decay du résonateur, ce qui va ranger progressivement
# la résonnance des notes du chime
decay = Sine(.1).range(.01, .15)

# 6 filtres complexes
rezos = ComplexRes(pluck, freqs, decay, mul=5).out()

def change_frequencies():
    "Change les 6 fréquences du chime"
    rezos.freq = [random.uniform(1000, 3000) for i in range(6)]

# Appel périodique pour changer les fréquences du chime toutes les 2 secondes
pat = Pattern(change_frequencies, 2).play()

# Affichage
sp = Spectrum(rezos)
sc = Scope(rezos)

s.gui(locals())
