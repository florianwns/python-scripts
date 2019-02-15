"""
Fait dodo

On utilise la librairie de gestion du temps
pour modifier la fréquence d'un PyoObject
"""
from pyo import *
import time
s = Server().boot()
a = Sine(440, 0, 0.1).out()
s.start()
for i in range(100):
    a.setFreq(440 + i * 10)
    time.sleep(0.1)
s.stop()
