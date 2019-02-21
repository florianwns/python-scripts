#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Les filtres passe-bas.

Pour ce premier exemple de filtrage, nous comparons le spectre de fréquences
de trois filtres passe-bas communs.

Tone: Filtre passe-bas de premier ordre IIR
ButLP: Filtre passe-bas de second ordre IIR (Butterworth)
MoogLP: Filtre passe-bas de de quatrième ordre IIR (paramètre de résonance)

En complément, les filtres passe-haut respectifs pour Tone et ButLP sont
Atone et ButHP. Un autre filtre passe-haut courant est l’objet DCBlock, qui
peut être utilisé pour supprimer une composante continue d’un signal audio.

L'exemple suivant présentera les filtres passe-bas.
"""
from pyo import *

s = Server().boot().start()

# Bruit blanc
n = Noise(mul=.5)

# Contrôle de la fréquence de coupure (cutoff frequency)
freq = Sig(1000)
freq.ctrl([SLMap(50, 5000, "lin", "value", 1000)], title="Cutoff Frequency")

# 3 filtres passe-bas différents
tone = Tone(n, freq)
butlp = ButLP(n, freq)
mooglp = MoogLP(n, freq)

# Interpolation avec les 3 filtres en entrée
sel = Selector([tone, butlp, mooglp]).out()
sel.ctrl(title="Filter selector (0=Tone, 1=ButLP, 2=MoogLP)")

# Affichage du spectre de l'interpolation
sp = Spectrum(sel)

s.gui(locals())
