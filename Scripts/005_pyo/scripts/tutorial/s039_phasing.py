"""
Le modulateur de phase.

L'objet Phaser implémente un nombre variable de filtres allpass de second ordre,
permettant de créer rapidement des effets de déphasage complexes.

Un modulateur de phase est un processus utilisé pour filtrer un signal en créant
une série de pics et de creux dans le spectre de fréquences. La position des
pics et des creux du signal affectée est généralement modulée de sorte qu'ils
varient dans le temps, créant ainsi un effet de balayage.

À cette fin, les 'phaser' incluent généralement un LFO.
https://en.wikipedia.org/wiki/Phaser_(effect)
Une unité de décalage de phase peut être construite à partir de zéro avec
l'objet Allpass2, qui implémente un filtre allpass de second ordre qui crée,
une fois ajouté à la source d'origine, une encoche dans le spectre.
"""
from pyo import *

s = Server().boot().start()

 # Simple fadein
fade = Fader(fadein=.5, mul=.2).play()

# Bruit rose
a = PinkNoise(fade)

# Ces LFOs modulent les arguments de fréquence `freq`, facteur de diffusion
# `spread`, et facteur de qualité/largeur de bande `q` de l'objet Phaser.
# Nous donnons une liste de deux fréquences pour créer des LFOs à deux flux,
# donc un effet de déphasage stéréo.
lf1 = Sine(freq=[.1, .15], mul=100, add=250)
lf2 = Sine(freq=[.18, .13], mul=.4, add=1.5)
lf3 = Sine(freq=[.07, .09], mul=5, add=6)

# Joue 20 modulateurs (num=20) de phase sur le bruit rose
b = Phaser(a, freq=lf1, spread=lf2, q=lf3, num=1, mul=.5).out()

# Affichage
sp = Spectrum([a, b])
sc = Scope([a, b])

s.gui(locals())
