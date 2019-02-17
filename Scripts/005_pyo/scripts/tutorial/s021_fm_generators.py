"""
Synthèse de modulation de fréquence.
Il existe deux objets dans la bibliothèque qui implémentent des algorithmes
de modulation de fréquence. Ces objets sont très simples, bien que puissants.
Il est également relativement simple de construire un algorithme FM
personnalisé, cela sera couvert dans les tutoriels sur les algorithmes de
synthèse personnalisés.

Utilisez le curseur "voice" de la fenêtre "Input interpolator" pour mixer
les deux sources. Utilisez les fenêtres du contrôleur pour modifier les
paramètres des algorithmes FM.
"""
from pyo import *

s = Server().boot().start()

# Impementation de l'algorithme de synthèse FM de Chowning
fm1 = FM(carrier=250, ratio=[1.5,1.49], index=10, mul=0.3)
fm1.ctrl()

# CrossFM implémente une synthèse de modulation de fréquence où
# la sortie des deux oscillateurs module la fréquence de l'autre
fm2 = CrossFM(carrier=250, ratio=[1.5,1.49], ind1=10, ind2=2, mul=0.3)
fm2.ctrl()

# Interpolation entre les signaux de FM
sel = Selector([fm1, fm2]).out()
sel.ctrl(title="Input interpolator (0=FM, 1=CrossFM)")

# Affichage de la source sélectionnée
sc = Scope(sel)
sp = Spectrum(sel)

s.gui(locals())
