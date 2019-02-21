#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateurs de bruits

Il y a trois générateurs de bruit dans la bibliothèque.
Ce sont le bruit blanc classique, le bruit rose et le bruit brun.

Noise: Générateur de bruit blanc, spectre plat.
PinkNoise: Générateur de bruit rose, atténuation de 3dB par octave.
BrownNoise: Générateur de bruit marron, atténuation de 6 dB par octave.
"""
from pyo import *

s = Server().boot().start()


# Bruit blanc
n1 = Noise(0.3)

# Bruit rose
n2 = PinkNoise(0.3)

# Bruit brun
n3 = BrownNoise(0.3)

# Interpolation entre les entrées pour produire une seule sortie
sel = Selector([n1, n2, n3]).out()
sel.ctrl(title="Input interpolator (0=White, 1=Pink, 2=Brown)")

# Affichage de la source sélectionnée
sc = Scope(sel)
sp = Spectrum(sel)

s.gui(locals())
