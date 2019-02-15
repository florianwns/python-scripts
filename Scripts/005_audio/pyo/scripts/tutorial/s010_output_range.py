"""
Plage de sortie

Presque tous les objets audio ont des attributs mul et add.
Ceux-ci sont définis à l'intérieur du PyoObject,
qui est la classe de base pour tous les objets générant un signal audio.
La page de manuel de PyoObject explique tous les comportements
communs aux objets audio.

Un signal audio produit des échantillons sous forme de nombres
à virgule flottante dans la plage -1 à 1.
Les attributs mul et add peuvent être utilisés pour modifier
la plage de sortie. Les utilisations courantes sont pour moduler
l'amplitude d'un son ou pour construire des signaux de contrôle tels
que des oscillateurs à basse fréquence.

Un raccourci pour manipuler automatiquement les attributs mul et add
est d'appeler la méthode range(min, max) du PyoObject.

Cette méthode définit les attributs mul et add en fonction des valeurs
de sortie min et max souhaitées. Cela suppose que le signal généré
est compris entre -1 et 1.
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
