#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Flux multi-canaux #2

Quand on utilise des listes de différentes tailles
pour créer des flux multi-canaux, la liste la plus longue défini
le nombre de flux, et les plus petites vont boucler pour combler les trous.

Cette particularité est très utile pour créer des objets complexes.
"""
from pyo import *

s = Server().boot().start()

# 12 flux avec différentes combinaisons de fréquences et de ratio
a = SumOsc(freq=[100, 150.2, 200.5, 250.7],
           ratio=[0.501, 0.753, 1.255],
           index=[.3, .4, .5, .6, .7, .4, .5, .3, .6, .7, .3, .5],
           mul=.05)

# Ajoute une réverbération au signal mixé en 2 flux (gauche, droite)
rev = Freeverb(a.mix(2), size=0.80, damp=0.70, bal=0.30).out()

s.gui(locals())
