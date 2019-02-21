#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Limiter la largeur de bande du filtre passe-bande.

Cet exemple illustre la différence entre un filtre passe-bande de second ordre
IIR simple et une cascade de 4 filtres passe-bande de second ordre.

Une cascade de quatre filtres passe-bande avec le paramètre Q élevé peut être
utilisée comme résonateur efficace sur le signal.
"""
from pyo import *

s = Server().boot().start()

# Bruit blanc
n = Noise(mul=.5)

# Contrôle de la fréquence de coupure (cutoff frequency)
freq = Sig(1000)
freq.ctrl([SLMap(50, 5000, "lin", "value", 1000)], title="Cutoff Frequency")

# Contrôle du facteur Q (facteur de qualité)
# https://fr.wikipedia.org/wiki/Facteur_de_qualit%C3%A9
q = Sig(5)
q.ctrl([SLMap(0.7, 20, "log", "value", 5)], title="Filter's Q")

# Filtre passe-bande de second ordre
bp1 = Reson(n, freq, q=q)

# 4 filtres passe-bande de second ordre en série
bp2 = Resonx(n, freq, q=q, stages=4)

# Interpolation avec les 2 filtres
sel = Selector([bp1, bp2]).out()
sel.ctrl(title="Filter selector (0=Reson, 1=Resonx)")

# Affichage du spectre de l'interpolation
sp = Spectrum(sel)

s.gui(locals())
