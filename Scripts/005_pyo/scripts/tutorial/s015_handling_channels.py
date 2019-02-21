#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gestion des canaux #1

Si un objet avec plusieurs flux est passé en paramètre d'un autre objet,
celui-ci sera de même longueur afin de traiter les flux passés
en paramètre. Il est très puissant de créer des traitement polyphoniques sans
copier de long morceaux de code, mais cela peut coûter cher au niveau
des ressources du processeur.

Dans cet exemple, nous créons une onde carrée à partir d'ondes sinusoïdales.
Après cela, un chorus est appliqué à la forme de l'onde résultante.
Si nous ne mélangeons pas l'onde carrée avant de la passer en argument, nous
aurons des dizaines d'objets Chorus dans la chaine de traitement.
Cela peut facilement saturer le processeur.
Le même résultat peut être obtenu avec un seul Chorus appliqué à la somme des
ondes. La méthode de mixage mix(voices) du PyoObject facilite la gestion des
canaux afin d'économiser le CPU. Ici nous mélangeons tous les flux en seulement
2 flux pour garder la stéréo puis les passons en paramètre de l'objet Chorus.
"""
from pyo import *

s = Server().boot().start()

# fréquence fondamentale et le nombre harmoniques
freq, n = 100, 20

# Génération des liste des fréquences harmoniques impaires, et des amplitudes
harms = [freq * i for i in range(1, n) if i%2]
amps = [0.33 / i for i in range(1, n) if i%2]

# Création d'une onde carré par synthèse additive
a = Sine(freq=harms, mul=amps)

# Mix des flux de 'a' avant traitement du Chorus
b = Chorus(a.mix(2), feedback=0.5).out()

# Affichage du nombres de flux de chaque objet
print("Nombre de flux contenus dans a:", len(a))
print("Nombre de flux contenus dans b:", len(b))

s.gui(locals())
