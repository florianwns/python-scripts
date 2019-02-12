"""
un peu de FM

Source :http://ajaxsoundstudio.com/pyo_on_bela_html/node05.html
"""
from pyo import *

s = Server().boot()

fcar = 250
rat = 0.499
fmod = fcar * rat
ind = LFO(freq=1, type=1, mul=.5, add=.5)
mod = Sine(freq=fmod, mul=fmod*ind*10)
# la frequence de la variable change de façon modulaire
# on lui passe un PyoObject, idem pour le volume avec mul
car = Sine(freq=fcar+mod, mul=ind*0.3).out()

s.gui(locals())
