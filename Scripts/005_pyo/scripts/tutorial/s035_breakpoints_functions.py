"""
Enveloppes multi-segments.

Les objets Linseg et Expseg dessinent une série de segments (linéaires ou
exponentiels) entre des points de rupture spécifiés.

Ces objets attendent l'appel de play() pour commencer à lire l'enveloppe.

Ils disposent de méthodes pour définir le mode boucle, appeler une
pause/lecture sans réinitialisation et remplacer les points d'arrêt.

La méthode graph() permet d’ouvrir un affichage de l’enveloppe actuelle afin
de l’éditer et de copier les points dans le presse-papiers :
    => Menu 'File' de l’affichage du graphique
    => 'Copy all Points ...'
Cela facilite l'exploration et le collage du résultat dans le script python
lorsque l'utilisateur est satisfait de l'enveloppe.
"""
from pyo import *
import random

s = Server().boot().start()

# Genèration aléatoire d'une liste de 10 points (temps, valeur)
t = 0
points = [(0.0, 0.0), (2.0, 0.0)]
for i in range(8):
    t += random.uniform(.1, .2)
    v = random.uniform(.1, .9)
    points.insert(-1, (t, v))

# Genèration d'une enveloppe d'amplitude à segments exponentiels à partir de
# la liste des 10 points générée ci-dessus
amp = Expseg(points, exp=3, mul=0.3)
amp.graph(title="Amplitude envelope")

sig = RCOsc(freq=[150,151], sharp=0.85, mul=amp).out()

# Une fonction linéaire pour faire varier la quantité de décalage de fréquence.
sft = Linseg([(0.0, 0.0), (0.5, 20.0), (2, 0.0)])
sft.graph(yrange=(0.0, 20.0), title="Frequency shift")

# Décalage de fréquence.
# http://ajaxsoundstudio.com/pyodoc/api/classes/effects.html#freqshift
fsg = FreqShift(sig, shift=sft).out()

# Applique une reverb sur l'ensemble des 2 signaux
rev = WGVerb(fsg+sig, feedback=0.9, cutoff=3500, bal=0.3).out()

def play_note():
    "Rejoue les enveloppes d'amplitude et de décalage de fréquences"
    amp.play()
    sft.play()

# Appel périodique de la fonction play_note() toutes les 2 secondes
pat = Pattern(play_note, time=2).play()

# Affichage
sc = Scope([sig, fsg])
sp = Spectrum([sig, fsg])

s.gui(locals())
