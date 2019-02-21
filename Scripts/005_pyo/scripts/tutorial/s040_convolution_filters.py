#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convolution circulaire.

La convolution circulaire permet d'implémenter des Filtre FIR très complexes,
dont le coût processeur est lié à la longueur de la réponse impulsionnelle du
filtre.

Filtre RIF (en anglais Finite Impulse Response filter ou FIR filter)
https://fr.wikipedia.org/wiki/Filtre_%C3%A0_r%C3%A9ponse_impulsionnelle_finie

Dans pyo, il existe une famille d'objets de filtre à réponse impulsionnelle
utilisant la convolution circulaire avec un noyau prédéfini :

- IRAverage: filtre de moyenne mobile
- IRFM: filtre de type FM
- IRPulse: filtre en peigne => comb filter en anglais
- RWinSinc: filtre qui utilise la convolution circulaire pour mettre en oeuvre
des filtres standards(lp, hp, hp, br) avec une réponse en bande passante très
plate et une atténuation nette.

Pour la convolution circulaire de base, utilisez l'objet Convolve avec un
PyoTableObject comme noyau.

Dans cet exemple, un bruit blanc est filtré par quatre impulsions extraites des
enregistrements du micro.

Jouer r1.play(), r2.play(), r3.play() ou r4.play() dans l'interpreter tout en
émettant du son dans le micro pour remplir les tables de réponse impulsionnelle.
Le curseur gère le morphing entre les quatre sons(noyaux).

Appelez t1.view(), t2.view(), t3.view() ou t4.view() pour afficher les tables
de réponses impulsionnelles.

Étant donné que la convolution circulaire est très coûteuse : TLEN, le nombre
d'échantillons des réponses impulsionnelles doit rester assez faible.
"""
from pyo import *

s = Server().boot().start()

# Longeur de la réponse impulsionnelle
TLEN = 512

# Conversion en secondes pour la création des tables de réponses impulsionnelles
DUR = sampsToSec(TLEN)

# Signal qui va être filtré
sf = Noise(.5)

# Signal venant du micro pour enregistrer les réponses impulsionnelles
inmic = Input()

# 4 tables et enregistreurs
t1 = NewTable(length=DUR, chnls=1)
r1 = TableRec(inmic, table=t1, fadetime=.001)

t2 = NewTable(length=DUR, chnls=1)
r2 = TableRec(inmic, table=t2, fadetime=.001)

t3 = NewTable(length=DUR, chnls=1)
r3 = TableRec(inmic, table=t3, fadetime=.001)

t4 = NewTable(length=DUR, chnls=1)
r4 = TableRec(inmic, table=t4, fadetime=.001)

# Interpolation entre les tables de réponses impulsionnelles
pha = Sig(0)
pha.ctrl(title="Impulse responses morphing")

# Morphing entre les 4 réponses impulsionnelles
res = NewTable(length=DUR, chnls=1)
morp = TableMorph(pha, res, [t1,t2,t3,t4])

# Convolution circulaire entre le bruit rose (excitation)
# et le noyau (morhing des réponses impulsionnelles IR)
a = Convolve(sf, table=res, size=res.getSize(), mul=.1).mix(2).out()

# Affichage
sc = Scope(a)
sp = Spectrum(a)

s.gui(locals())
