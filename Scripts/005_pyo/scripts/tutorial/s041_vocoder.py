"""
Vocodeur : effet d’analyse/resynthèse.

Un vocodeur est un processus d’analyse/resynthèse qui utilise l’enveloppe
spectrale d’un premier son pour modeler le spectre d’un second son.
Habituellement et pour de meilleurs résultats, le premier son doit présenter un
spectre dynamique(fréquences et amplitudes) et le second son doit contenir un
spectre riche et stable.

Dans cet exemple, les LFOs sont appliqués à chaque arguments de l'objet
Vocoder pour démontrer une grande plage des effets sonores que l'utilisateur
peut obtenir avec un vocodeur.

http://ajaxsoundstudio.com/pyodoc/api/classes/filters.html?highlight=vocoder#pyo.Vocoder
"""
from pyo import *
from random import random
import os

s = Server().boot().start()

# Son avec un spectre dynamique
folder = os.path.dirname(os.path.abspath(__file__)) + "/../../sounds/"
filepath = folder + "baseballmajeur_m.aif"

# Lecture du son avec un légère variation de vitesse sur le canal de droite
spktrm = SfPlayer(filepath, speed=[1,1.001], loop=True)

# Bruit blan, le second son avec une spectre stable et bien plat
excite = Noise(0.2)

# 4 LFOs qui modulent chaque paramètre du Vocoder
lf1 = Sine(freq=0.1, phase=random()).range(60, 100)
lf2 = Sine(freq=0.11, phase=random()).range(1.05, 1.5)
lf3 = Sine(freq=0.07, phase=random()).range(1, 20)
lf4 = Sine(freq=0.06, phase=random()).range(0.01, 0.99)

# Le Vocoder avec ces différentes paramètres
voc = Vocoder(spktrm, excite, freq=lf1, spread=lf2, q=lf3, slope=lf4, stages=32).out()

# Affichage
sp = Spectrum([spktrm, voc])
sc = Scope([spktrm, voc])

s.gui(locals())
