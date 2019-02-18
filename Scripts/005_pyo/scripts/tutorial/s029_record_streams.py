"""
Enregistrement de flux audio individuels sur le disque.
L'objet 'Record' peut être utilisé pour enregistrer des flux audio spécifiques
d'une performance. Il peut être utile d’enregistrer un son sur plusieurs pistes
pour faciliter le post-traitement d’une partie à l’autre.
Cet exemple enregistre les parties basse, moyenne et haute dans trois fichiers
séparés sur le bureau de l'utilisateur.

Les arguments fileformat et sampletype sont les mêmes que dans la méthode
'recordOptions' du serveur.
"""
from pyo import *
import os

s = Server().boot()

# Définit les chemins des fichiers
path = os.path.join(os.path.expanduser("~"), "Desktop")
bname = os.path.join(path, "bass.wav")
mname = os.path.join(path, "mid.wav")
hname = os.path.join(path, "high.wav")

# Crée une enveloppe d'amplitude
amp = Fader(fadein=1, fadeout=1, dur=10, mul=0.3).play()

# Bass
blfo = Sine(freq=[0.15, 0.16]).range(78, 82)
bass = RCOsc(freq=blfo, mul=amp).out()

# Mid
mlfo = Sine(freq=[0.18, 0.19]).range(0.24, 0.26)
mid = FM(carrier=1600, ratio=mlfo, index=5, mul=amp*0.3).out()

# High
hlfo = Sine(freq=[0.1, 0.11, 0.12, 0.13]).range(7000, 8000)
high = Sine(freq=hlfo, mul=amp*0.1).out()

# Créer les enregistreurs de flux
brec = Record(bass, filename=bname, chnls=2, fileformat=0, sampletype=1)
mrec = Record(mid, filename=mname, chnls=2, fileformat=0, sampletype=1)
hrec = Record(high, filename=hname, chnls=2, fileformat=0, sampletype=1)

# Après 10.1 secondes, les enregistreurs seront automaitquement détruit
# Cela va déclencher leur méthodes stop et proprement fermé les fichiers sons
clean = Clean_objects(10.1, brec, mrec, hrec)

# Commence l'horloge internal de Clean_objects. Utilise son propre thread
clean.start()

# Lance le Server, afin d'être synchronisé avec le processus de suppression.
s.start()

s.gui(locals())
