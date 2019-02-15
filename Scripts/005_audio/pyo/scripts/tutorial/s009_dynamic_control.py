"""Contrôle dynamique

Avec pyo, il est facile d’essayer rapidement une combinaison de paramètres
avec la fenêtre du contrôleur déjà configurée pour chaque objet.
Pour ouvrir la fenêtre du contrôleur, appelez simplement la méthode ctrl()
sur l'objet que vous souhaitez contrôler.
"""
from pyo import *

s = Server().boot()
s.amp = 0.1

# Crée deux objets par channel
a = FM().out(0) # Gauche
b = FM().out(1) # Droite

# Ouvre les fenêtre de contrôle (WxWidgets)
a.ctrl(title="FM, Gauche")
b.ctrl(title="FM, Droite")

s.gui(locals())
