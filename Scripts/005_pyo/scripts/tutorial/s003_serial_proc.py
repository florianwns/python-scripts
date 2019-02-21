#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Traitement audio en série

Cet exemple montre comment chaîner des traitements audio sur une source unique.
Chaque objet de traitement (c-a-d ceux qui modifient une source audio)
ont un premier argument appelé "input".
L'argument "input" prend l'objet audio à traiter.

Notez la variable d'entrée donnée à chaque harmoniseur.
"""
from pyo import *

s = Server().boot()
s.amp = 0.1

# Crée une sinusoïde comme source de traitement
a = Sine().out()

# Passes l'onde à travers l'objet harmonizer.
h1 = Harmonizer(a).out()

# Puis passes l'onde harmonisée à travers un autre objet harmonizer.
h2 = Harmonizer(h1).out()

# Etc...
h3 = Harmonizer(h2).out()

# Etc...
h4 = Harmonizer(h3).out()

s.gui(locals())
