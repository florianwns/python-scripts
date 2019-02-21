#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Portamento exponentiel avec temps de montée et de descente.

L'objet Port est conçu pour filtrer en mode 'passe-bas' un signal audio avec
différents coefficients pour les signaux ascendants et descendants. Un filtre
passe-bas est un moyen efficace de créer une rampe exponentielle à partir d'un
signal contenant des changements abrupts. Les coefficients croissant et
décroissant sont contrôlés en secondes.
"""
from pyo import *

s = Server().boot().start()

# Choisit une nouvelle valeur 2 fois par seconde
pick = Choice([200,250,300,350,400], freq=2)

# Affiche la fréquence choisie
pp = Print(pick, method=1, message="Frequency")

# Ajoute un portamento exponentiel sur une cible audio et désaccorde
# un peu la 2eme fréquence. Attaque courte pour les notes montantes et long
# relâchement pour les notes tombantes.
freq = Port(pick, risetime=0.001, falltime=0.25, mul=[1, 1.005])

# Contrôle pour jouer avec le portamento
freq.ctrl()

# Joue une onde toute simple
sig = RCOsc(freq, sharp=0.7, mul=0.3).out()

# Affichage
sc = Scope([sig, freq])
sp = Spectrum(sig)

s.gui(locals())
