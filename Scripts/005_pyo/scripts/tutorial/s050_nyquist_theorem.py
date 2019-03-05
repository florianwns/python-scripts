#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Théorème de Nyquist
"""
from pyo import *

# Pour un serveur avec 2 canaux en mode duplex (entrée, sortie)
# Un taux d'échantillonage de 48Khz et une taille de buffer de 512 échantillons
s = Server(sr=48000, nchnls=2, buffersize=512, duplex=1)
s.boot().start()

# Afin de reconstruire un signal, la fréquence d'échantillonage doit être le
# double de la fréquence du signal échantillonné.

# Si on tente d'enregistrer un signal de 30Khz dans un convertisseur travaillant
# en 48Khz, on obtiendra alors un signal de 18khz => 48 - 30 = 18

# la plus haute fréquence pouvant être représentée dans un système en 48Khz
# est donc sr/2 => 24khz

s.gui(locals())
