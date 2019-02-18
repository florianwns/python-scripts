"""
Conversion entre nombre et flux audio.

L'objet Stream est un nouveau type introduit par pyo pour représenter un signal
audio en tant que vecteur de nombre à virgule. Il est parfois utile de pouvoir
convertir des nombres simples (nombres flottants ou entiers de Python) en signal
audio ou d’extraire des nombres d’un flux audio.

L'objet Sig convertit un nombre en flux audio.

La méthode PyoObject.get () extrait un nombre à virgule d’un flux audio.
"""
from pyo import *
import os

s = Server().boot().start()

# Un entier
anumber = 100

# Conversion d'un nombre en flux audio : vecteur de nombre à virgule (float)
astream = Sine(anumber)

# Utiliser Print() pour afficher un flux audio
pp = Print(astream, interval=0.1, message="Audio stream value")

# Utiliser la méthode get() pour extraire un nombre à virgule d'un flux audio.
print("Float from audio stream : ", astream.get())

s.gui(locals())
