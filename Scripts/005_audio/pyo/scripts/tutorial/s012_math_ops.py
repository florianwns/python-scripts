"""
Les opérateurs mathématique

Ce script montre comment un PyoObject reagit quand il est utilisé
au sein d'une expression arithmétique

La multiplication '*', l'addition '+', la division '/' et la soustraction '-'
peuvent être appliqué entre des PyoObject et des nombresself.
Cela renvoie un objet factice qui contient le résultat de l'opération.

Un object factice n'est qu'un espace réservé pour garder en mémoire
les opérations arithmétiques sur les objets audio.

les PyoObject peuvent être aussi utilisé avec l'exposant '**', le modulo '%'
et la négation '-'.
"""
from pyo import *

s = Server().boot().start()

# Création d'un sinusoîde de 1000 hz
a = Sine()

# Création d'un objet factice 'b' avec attribut 'mul' à 0.5
b = a * 0.5
#b.out()

# Imprime l'instance de classe
print(b)

# Création d'un modulation en anneaux entre deux PyoObjet
# et met à l'échelle l'amplitude du signal résultant
c = Sine(300)
d = a * c * 0.3
d.out()

# Les PyoObjet peuvent être utilisés avec l'operator **
e = c ** 10 * 0.4
e.out(1)

# Affiche les signaux
sp =  Spectrum([a, c, d, e])
sc =  Scope([a, c, d, e])


s.gui(locals())
