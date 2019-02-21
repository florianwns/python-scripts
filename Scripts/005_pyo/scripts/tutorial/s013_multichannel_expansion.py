#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Flux multi-canaux #1

La compréhension de listes est une technique puissante
pour générer plusieurs flux audio à la fois.

Qu'est qu'un flux ?
===================

Un flux est un canal d'échantillons monophonique.
C'est la structure de base sur laquelle tout la librairie PYO est construite.
Tout PyoObject peut gérer autant de flux que nécessaire pour représenter le
processur défini. Lorsqu'un objet polyphonique (c-a-d plusieurs flux)
est inivité à envoyer ses signaux en sortie, le serveur utilise les arguments
(chnl et inc) et la méthode out() pour répartir les flux sur les canaux de
sortie disponibles.


Preque tous les attributs de tous les objets acceptent une liste de valeurs
au lieu d'une valeur unique. L'objet créera en interne le même nombre
de flux que la longueur de la liste donnée en paramètre au moment de
l'initialisation.  Chaque valeur de la liste est utilisé pour générer un flux.
Les listes passées en paramètres peuvent avoir de longueurs différentes dans ce
cas les listes les plus courtes boucleront en décalage
par rapport au plus longues.

Un PyoObject est considéré comme une liste.
La méthode len() renvoie le nombre de flux gérés par l'objet
Cette fonctionnalité est donc utile pour créer une chaîne polyphonique.
"""
from pyo import *

s = Server().boot().start()

## Utilisation de flux multi-canaux pour créer une onde carrée
# fréquence fondamentale et et nombre harmoniques
freq, n = 100, 20

# Génération de la liste des fréquences harmoniques impaires
harms = [freq * i for i in range(1, n) if i%2]
# Génération de la liste des amplitudes
amps = [0.33 / i for i in range(1, n) if i%2]

# Création de toutes les ondes sinusoïdales à la fois
a = Sine(freq=harms, mul=amps)
# Affiche le nombre de flux gérés par 'a'
print(len(a))

# La méthode mix(voices) définie in PyoObject mixe l'ensemble des flux
# sur un certains nombre de voix
b = a.mix(voices=1).out()

# Affiche l'onde de forme b
sc = Scope(b)

s.gui(locals())
