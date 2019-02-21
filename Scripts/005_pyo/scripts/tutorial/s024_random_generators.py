#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateurs aléatoires.

La catégorie des générateurs aléatoire de pyo contient de nombreux objets
pouvant être utilisés à différentes fins. Cette catégorie mérite vraiment
d'être explorée.

Dans ce tutoriel, nous utilisons trois objets aléatoires (Choice, Randi,
RandInt) pour contrôler les hauteurs, l'amplitude et le ton d'un synthé simple.

Nous reviendrons sur les générateurs aléatoires lorsque nous parlerons
d'algorithmes musicaux.
"""
from pyo import *

s = Server().boot().start()

# 2 flux de notes MIDI choisis au hasard dans une liste prédéfinie,
# afin de réaliser une stéréo sur des rythmes différents
mid = Choice(choice=[60,62,63,65,67,69,71,72], freq=[2,3])

# 2 petits tremblements qui seront appliqués sur les flux de fréquence.
# Randi génère un nombre aléatoire entre 'min' et 'max' à la fréquence 'freq'
# et fait une interpolation
jit = Randi(min=0.993, max=1.007, freq=[4.3,3.5])

# Convertit les notes MIDI en fréquences et applique le petit tremblement
fr = MToF(mid, mul=jit)

# Choisit une valeur pour la brillance du synthé comprise entre 0 et 0.15
# toutes les 4 secondes.
fd = Randi(min=0, max=0.15, freq=0.25)

# RandInt génère un nombre entier pseudo-aléatoire compris entre 0 et max
# valeurs à une fréquence spécifiée par le paramètre 'freq'.
# on obtient donc des nombres compris entre 8 et 14 toutes les secondes
sp = RandInt(max=6, freq=1, add=8)

# Crée un LFO oscillant entre 0 et 0.4
# avec une fréquence qui change varie entre 8 et 14 Hz
# à chaque seconde grâce à RandInt
amp = Sine(sp, mul=0.2, add=0.2)

# Un simplé synthé...
a = SineLoop(freq=fr, feedback=fd, mul=amp).out()

# Affichage
sc = Scope(a)
sp2 = Spectrum(a)

s.gui(locals())
