#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Oscillateurs dont le spectre est maintenu sous la fréquence de Nyquist
cf : https://fr.wikipedia.org/wiki/Fr%C3%A9quence_de_Nyquist

Ce script présente un objet (mal nommé "LFO" mais il est trop tard pour changer
de nom !) qui implémente différentes formes d’ondes à bande limitée.
Un signal à bande limitée est un signal dont aucun des partiels ne dépasse la
fréquence de Nyquist.

L’objet LFO, malgré son nom, peut être utilisé comme oscillateur standard,
avec des fréquences fondamentales très élevées.
Aux basses fréquences (inférieures à 20 Hz), cet objet donnera un véritable LFO
de formes différentes.

Le curseur "type" dans la fenêtre du contrôleur
permet de choisir entre ces formes d'onde particulières:

 - 0 : Saw up (default)
 - 1 : Saw down
 - 2 : Square
 - 3 : Triangle
 - 4 : Pulse
 - 5 : Bipolar pulse
 - 6 : Sample and hold
 - 7 : Modulated Sine

"""
from pyo import *

s = Server().boot().start()

# Fréquence fondamentale
freq = 187.5

# LFO appliqué a l'attribut "sharp" (tranchant)
lfo = Sine(.2, mul=0.5, add=0.5)

# Différentes formes d'onde à bande limitée
osc = LFO(freq=freq, sharp=lfo, mul=0.4).out()
osc.ctrl()

# Affichage
sc = Scope(osc)
sp = Spectrum(osc)

s.gui(locals())
