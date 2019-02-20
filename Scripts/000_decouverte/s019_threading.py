#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Utilisation simple des Threads
"""
from threading import Thread
from random import random
from time import sleep



class Compteur(Thread):
    """
    Un simple compteur dans un thread séparé
    """
    def __init__(self, n, label="Thread =>"):
        Thread.__init__(self)
        self._n = n
        self._label = label

    def run(self):
        for i in range(self._n):
            print(self._label, i)
            # facilite la lecture de l'affichage
            sleep(random())


# Creation du thread
n = 10
a = Compteur(n, "Thread 1 =>").start()
b = Compteur(n, "Thread 2 =>").start()


# l'instruction est exécutée en quelques millisecondes
# quelque soit la durée du thread
for i in range(n):
    print("Programme =>", i)
    sleep(random())
