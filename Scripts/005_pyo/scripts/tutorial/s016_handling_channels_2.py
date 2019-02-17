"""
Gestion des canaux #2

Dans un environnement multicanal, nous pouvons choisir avec soin quel flux
ira vers quel canal de sortie. Pour ce faire nous utilisons les arguments
chnl et inc de la méthode out().

chnl : sortie physique affectée au premier flux audio de l'objet
inc : valeur d'incrément de canal de sortie
"""
from pyo import *

# Crée un serveur avec 8 canaux
s = Server(nchnls=8).boot()

# Génère une onde sinusoïdale
a = Sine(freq=500, mul=0.3)

# Mixe l'onde sur 4 flux
b = a.mix(4)

# Dirige les flux vers les sorties 0, 2, 4 et 6
b.out(chnl=0, inc=2)

s.gui(locals())
