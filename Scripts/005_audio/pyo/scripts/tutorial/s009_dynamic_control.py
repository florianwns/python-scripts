"""Contrôle dynamique

source : http://ajaxsoundstudio.com/pyodoc/examples/02-controls/02-dynamic-control.html
"""
from pyo import *

s = Server().boot()
s.amp = 0.1

# Crée deux objets par channel
a = FM().out(0) # Gauche
b = FM().out(1) # Droite

# Ouvre les fenêtre de contrôle (WxWidgets)
a.ctrl(title="FM, Gauche")
b.ctrl(title="FM, Droite")

s.gui(locals())
