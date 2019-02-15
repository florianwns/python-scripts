"""Plage de sortie

source : http://ajaxsoundstudio.com/pyodoc/examples/02-controls/03-output-range.html
"""
from pyo import *

s = Server().boot().start()

# l'attribut 'mul' multiplie chaque sample par sa value
a = Sine(freq=100, mul=0.1)

# l'attribut 'add' ajoute un décalage à chaque sample
# la multiplication est effectué avant l'addition
b = Sine(freq=100, mul=0.5, add=0.5)

# Utiliser la méthode range(min, max) permet de trouver automatiquement
# les deux attributs `mul` et `add` et de les appliquer au PyoObject
c = Sine(freq=100, mul=0.3).range(-0.25, 0.5)

# L'oscillateur affiche les formes d'ondes 
sc = Scope([a, b, c])

s.gui(locals())
