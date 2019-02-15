"""Canal de sortie

source : http://ajaxsoundstudio.com/pyodoc/examples/01-intro/05-output-channels.html
"""
from pyo import *

s = Server().boot()
s.amp = 0.1

# Crée une source de bruit blanc
n = Noise()

# Envoie the basses fréquences (en dessous de 1Khz) vers la gauche
lp = ButLP(n).out() # 0 est  l'argument par défaut

# Envoie les hautes fréquences (au dessus de 1Khz) vers la droite
hp = ButHP(n).out(1)

s.gui(locals())
