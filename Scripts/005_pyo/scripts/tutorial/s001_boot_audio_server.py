#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Démarrage serveur

Comment on démarre le serveur de PYO ?
"""
from pyo import *

# Crée un serveur avec les paramètres par défaut.
# Voir le manuel pour changer le taux d’échantillonnage,
# la taille du buffer, le nombre de canaux ou l'un des autres paramètres.
s = Server()

# Démarre le serveur. cette étape initialise les flux audio et MIDI.
# Si besoin, les configurations audio et MIDI doivent être effectuées
# avant cet appel.
s.boot()

# Démarre le serveur. Cette étape active la boucle de traitement du serveur.
s.start()

# Ici, on écrit la chaîne de traitement...

# L'objet Serveur fournit une interface utilisateur graphique avec la méthode
# gui(). L'un de ses objectifs est de maintenir le programme en vie
# pendant le calcul des échantillons au fil du temps. Si le dictionnaire
# variables locales est donné en argument grâce à la fonction locals(),
# l'utilisateur peut continuer à envoyer des commandes à l'interpréteur python
# à partir de l'interface graphique.
s.gui(locals())
