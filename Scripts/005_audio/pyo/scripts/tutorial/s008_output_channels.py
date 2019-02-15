"""
Canal de sortie

Le moyen le plus simple de choisir le canal de sortie où envoyer le son
consiste à lui donner le premier argument de la méthode out().
En fait, la signature de la méthode out() se lit comme suit:

.out(chnl=0, inc=1, dur=0, delay=0)

chnl est la sortie où envoyer le premier canal audio(flux) de l'objet.
inc est l'incrément de sortie pour les autres canaux audio.
dur est la durée de vie, exprimée en secondes, du traitement.
delay est un délai, en secondes, avant l'activation du processus.
Une durée de 0 signifie pour toujours.
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
