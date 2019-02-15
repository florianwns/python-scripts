"""Traitements multiples à partir d'une seule source.

Cet exemple montre comment lire différents objets audio en parallèle.
Chaque objet de traitement (c-a-d ceux qui modifient une source audio)
ont un premier argument appelé "input".
L'argument "input" prend l'objet audio à traiter.

Notez la variable d'entrée donnée à chaque objet de traitement
et leur appel respectif à la méthode out() permettant d'envoyer
leurs échantillons à la sortie audio.
"""
from pyo import *

s = Server().boot()
s.amp = 0.1

# Creates a sine wave as the source to process.
a = Sine()

# Passes the sine wave through an harmonizer.
hr = Harmonizer(a).out()

# Also through a chorus.
ch = Chorus(a).out()

# And through a frequency shifter.
sh = FreqShift(a).out()

s.gui(locals())
