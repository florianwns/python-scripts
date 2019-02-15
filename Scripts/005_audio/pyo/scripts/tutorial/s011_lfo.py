"""
Contrôler l'audio avec des lfo

Une des choses les plus importantes en informatique musicale
est la trajectoire prise par les paramètres dans le temps.
Cela donne vie au son !

Un moyen de créer des valeurs dynamiques consiste à connecter
un oscillateur basse fréquences à l'attribut d'un objet.

source : http://ajaxsoundstudio.com/pyodoc/examples/02-controls/04-building-lfo.html
"""
from pyo import *

s = Server().boot().start()

# Création d'un bruit blanc
n = Noise()

# Création d'une LFO qui oscille +/- 500 autour des 1000 Hz (Filtre des fréquences)
lfo1 = Sine(freq=0.1, mul=500, add=1000)
# Création d'une LFO qui oscille entre 2 et 8 Hz (Facteur Q, largeur de bande)
lfo2 = Sine(freq=.4).range(2, 8)
# Création d'un filtre passe-bande dynamique appliqué au bruit
bp1 = ButBP(n, freq=lfo1, q=lfo2).out()

# L'object LFO fournit plus de formes d'ondes qu'une simple sinusoïde.

# Création d'une dent de scie descendante oscillante +/- 1000
# autour des 1200 Hz (Filtre des fréquences)
lfo3 = LFO(freq=.25, type=1, mul=1000, add=1200)
# Création d'un signal carré oscillant entre 4 et 12 Hz  (Facteur Q)
lfo4 = LFO(freq=4, type=2).range(4, 12)
# Création d'un filtre passe-bande dynamique appliqué au bruit
bp2 = ButBP(n, freq=lfo3, q=lfo4).out(1)

s.gui(locals())
