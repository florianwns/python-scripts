"""
Lecture de fichier audio à partir du disque

SfPlayer et ses amis lisent les échantillons d'un fichier à partir du disque
avec un contrôle sur la vitesse de lecture et le bouclage.

Les différents lecteurs :
- SfPlayer: Lit de nombreux formats de fichiers son à partir du disque.
- SfMarkerLooper: lit les AIFF avec des repères dans le fichier boucleur.
- SfMarkerShuffler: lit les AIFF avec un brasseur de fichiers sonores.

Note :
Lire un fichier son sur un disque peut économiser beaucoup de RAM,
en particulier si le fichier son est volumineux,
mais cela coûte plus cher en ressources processeur que de charger le fichier
son en mémoire lors du premier passage.
"""
from pyo import *
import os

s = Server().boot().start()

# récupère le chemin du fichier son
folder = os.path.dirname(os.path.abspath(__file__)) + "/../../sounds/"
path = folder + "transparent.aif"

# Lecture en stéréo avec 2 vitesses de lectures différentes à gauche et à droite
sf = SfPlayer(path, speed=[1, 0.5], loop=True, mul=0.4).out()

s.gui(locals())
