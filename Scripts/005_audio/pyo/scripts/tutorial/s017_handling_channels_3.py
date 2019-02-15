"""
Gestion des canaux #3

Randomisation des sorties en multicanal

Si l'attribut chnl est négatif, les flux commencent sur le canal 0, mais
leur distribution se fait de manière aléatoire.
"""
from pyo import *

s = Server().boot().start()

amps = [.05,.1,.15,.2,.25,.3,.35,.4]

# Génère 8 ondes sinusoïdales grâce à la liste des amplitudes
a = Sine(freq=500, mul=amps)

# Mélange les canaux de sortie physique
a.out(chnl=-1)

s.gui(locals())
