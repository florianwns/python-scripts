"""
Portamento, glissando, ramping.

L'objet SigTo permet de créer un glissando entre la valeur actuelle et la valeur
cible, dans un délai défini par l'utilisateur. La valeur cible peut être un
float ou un autre PyoObject. Une nouvelle rampe est créée chaque fois que la
valeur cible change.

Aussi :

L'objet VarPort agit de manière similaire mais ne fonctionne qu'avec des float
et peut appeler une fonction callback définie par l'utilisateur lorsque la
rampe atteint la valeur cible.

La méthode PyoObject.set() est une autre façon de créer une rampe pour tout
paramètre donné qui accepte un signal audio mais qui n’est pas déjà contrôlé
avec un PyoObject.
"""
from pyo import *
import os

s = Server().boot().start()

# Choisit une nouvelle valeur 2 fois par seconde
pick = Choice([200,250,300,350,400], freq=2)

# Affiche la fréquence choisie
pp = Print(pick, method=1, message="Frequency")

# temps maximum pour atteindre la nouvelle fréquence
t_max = 0.5

# Ajoute un petit portamento sur une cible audio et désaccorde la 2eme fréquence
freq = SigTo(pick, time=t_max, mul=[1, 1.005])

# Contrôle pour jouer avec le temps du portamento
freq.ctrl([SLMap(0, t_max, "lin", "time", t_max, dataOnly=True)])

# Rampe linéaire d'amplitude allant de 0.0 à 0.3 en 5 secondes.
amp = SigTo(init=0.0, value=0.3, time=5.0)

# Joue une onde toute simple
sig = RCOsc(freq, sharp=0.7, mul=amp).out()

# Affichage
sc = Scope(sig)
sp = Spectrum(sig)


s.gui(locals())
