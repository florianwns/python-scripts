"""Le “hello world” de PYO !

Permet de jouer un onde de 1000 Hz
"""
from pyo import *

# Créer un serveur audio et le démarre
s = Server().boot()

# Démarre le calcul des échantillons des objets
s.start()

# Descend le gain de 20 dB.
s.amp = 0.1

# Créer une onde sinusoîdale
a = Sine()

# Active le calcul des échantillons de l'objet
a.play()

# Active le calculs des échantillons de l'object
# en indiquant les sorties audio en paramètre
a.out([0,1])

# Arrête le calcul des échantillons de l'object
# permet d'économis le CPU
# a.stop()

# ouvre un fenêtre de contrôle pour l'object
a.ctrl()

# Ouvre l'interface graphique en lui passant
# l'ensemble des variables locales
# Nécessaire pour ne pas que le programme ne se termine
s.gui(locals())
