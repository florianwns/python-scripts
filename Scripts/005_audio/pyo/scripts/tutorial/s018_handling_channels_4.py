"""Gestion des canaux #4

Si l'attribut chnl est une liste, les flux seront distribués sur le canaux
respectivement à la liste passée en paramètre.
"""
from pyo import *

s = Server().boot().start()

# Crée un serveur avec 8 canaux
s = Server().boot()

amps = [.05,.1,.15,.2,.25,.3,.35,.4]

# Génère 8 ondes sinusoïdales grâce à la liste des amplitudes
a = Sine(freq=500, mul=amps)

# Défini l'ordre des canaux de sorties
a.out(chnl=[3,4,2,5,1,6,0,7])

s.gui(locals())
