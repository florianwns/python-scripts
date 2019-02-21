#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Récupérer l'évènement de fin de fichier depuis l'objet SfPlayer.

Cet exemple montre comment utiliser l'évènement de fin de fichier de l'objet
SfPlayer pour déclencher une autre lecture (éventuellement avec un autre son,
une autre vitesse, etc.).

Lorsqu'un SfPlayer atteint la fin du fichier, il envoie un déclencheur
(que vous pourrez reproduire ultérieurement) que l'utilisateur peut récupérer
avec la syntaxe suivante: variable_name[“trig”]
"""
from pyo import *
import random, os

s = Server().boot().start()

# Banque de sons
# récupère le chemin des fichiers sons
folder = os.path.dirname(os.path.abspath(__file__)) + "/../../sounds/"
sounds = ["alum1.wav", "alum2.wav", "alum3.wav", "alum4.wav"]

# Crée 2 lecteurs audio, dirigé vers la gauche et la droite
sfL = SfPlayer(folder+sounds[0], speed=1, mul=0.5).out()
sfR = SfPlayer(folder+sounds[0], speed=1, mul=0.5).out(1)

# Fonction qui choisit un sons aléatoire pour le lecteur de gauche
def newL():
    sfL.path = folder + sounds[random.randint(0, 3)]
    sfL.speed = random.uniform(0.75, 1.5)
    sfL.out()

# Le déclencheur du signal "end-of-file"lié à la fonction "newL"
tfL = TrigFunc(sfL["trig"], newL)

# Fonction qui choisit un sons aléatoire pour le lecteur de droite
def newR():
    sfR.path = folder + sounds[random.randint(0, 3)]
    sfR.speed = random.uniform(0.75, 1.5)
    sfR.out(1)

# Le déclencheur du signal "end-of-file"lié à la fonction "newR"
tfR = TrigFunc(sfR["trig"], newR)

s.gui(locals())
