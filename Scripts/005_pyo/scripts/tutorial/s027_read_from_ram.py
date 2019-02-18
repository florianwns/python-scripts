"""
Lecture d'un fichier audio depuis la RAM.

La lecture d’un fichier son depuis la RAM offre l’avantage d’avoir un accès très
rapide à tous les échantillons chargés. Ceci est très utile pour de nombreux
processus, tels que la granulation, la création de boucles, la création
d’enveloppes et de formes d’ondes, etc.

Le moyen le plus simple de charger un son dans la RAM consiste à utiliser
l'objet SndTable. Cet exemple charge un fichier son et le lit en boucle.
Nous verrons plus tard des processus plus évolués ...
"""
from pyo import *
import random, os

s = Server().boot().start()

# récupère le chemin des fichiers sons
folder = os.path.dirname(os.path.abspath(__file__)) + "/../../sounds/"
path = folder + "/transparent.aif"

# Charge le fichier son dans la RAM. Les points de départ et d'arrivée
# peut être contrôlés avec les arguments "start" et "stop".
t = SndTable(path)

# Crée une copie du fichier et inverse le signal dans le temps
t_reversed = t.copy().reverse()

# Récupère la fréquence relative à la longueur de la table.
freq = t.getRate()

# Lecture des fichiers stockées en mémoire
osc = Osc(table=[t, t_reversed], freq=freq, phase=0, mul=0.4).out()

s.gui(locals())
