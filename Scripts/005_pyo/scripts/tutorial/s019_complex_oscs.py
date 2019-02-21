#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Oscillateurs à spectres complexes

Ce tutoriel présente quatre objets de la bibliothèque qui sont utiles pour
générer des spectres complexes par synthèse.

Blit: générateur de train à impulsions avec contrôle du nombre d'harmoniques.
RCOsc: approximation d'un circuit RC (un condensateur et une résistance en série).
SineLoop: Oscillateur à onde sinusoïdale avec retour.
SuperSaw: émulateur Supersaw Roland JP-8000.

Utilisez le curseur "voice" de la fenêtre "Input interpolator" pour interpoler
les quatre formes d'onde.
Chacune d'elle a un LFO appliqué à l'argument de fréquence.
"""
from pyo import *

s = Server().boot().start()

# Fréquence fondamentale
freq = 187.5

# Impulse train generator :
# Synthèse de train d'impulsions à bande limitée
# Générateur de train d'impulsions avec contrôle du nombre d'harmoniques dans
# le spectre, ce qui donne des oscillateurs avec un aliasing très faible
lfo1 = Sine(.1).range(1, 50)
osc1 = Blit(freq=lfo1, harms=lfo1, mul=0.3)

# RC circuit :
# Un circuit RC est un condensateur et une résistance en série,
# donnant une croissance logarithmique suivie d'une décroissance exponentielle.
lfo2 = Sine(.1, mul=0.5, add=0.5)
osc2 = RCOsc(freq=freq, sharp=lfo2, mul=0.3)

# SineLoop :
# La sortie de l'oscillateur, multipliée par le retour, est ajoutée à
# l'incrément de position et peut être utilisée pour contrôler lanbrillance
# de l'oscillateur.
lfo3 = Sine(.1).range(0, .18)
osc3 = SineLoop(freq=freq, feedback=lfo3, mul=0.3)

# Roland JP-8000 Supersaw emulator :
# Cet objet implémente une émulation de l'algorithme du Roland JP-8000.
# La structure de la forme d'onde est réalisée à partir de 7 oscillateurs
# en dents de scie désaccordés les uns avec les autres sur une période donnée.
# Il permet de contrôler la profondeur de la dissonance et l'équilibre entre
# les oscillateurs centraux et latéraux.
lfo4 = Sine(.1).range(0.1, 0.75)
osc4 = SuperSaw(freq=freq, detune=lfo4, mul=0.3)

# Permet de faire une interpolation entre les Oscillateur passés en paramètre
sel = Selector(inputs=[osc1, osc2, osc3, osc4])
sel.ctrl(title="Input interpolator (0=Blit, 1=RCOsc, 2=SineLoop, 3=SuperSaw)")

# Mixage de l'interpolation en stéréo
a = sel.mix(2).out()

# Affichage de la source sélectionné
sc = Scope(sel)
sp = Spectrum(sel)

s.gui(locals())
