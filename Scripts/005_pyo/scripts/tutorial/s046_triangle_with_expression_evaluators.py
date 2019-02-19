"""
Un signal triangulaire avec l'évaluateur d'expression

Algorithme : http://ajaxsoundstudio.com/pyodoc/api/classes/expression.html
"""
from pyo import *

s = Server().boot().start()

# Définition du traitement audio
proc = '''
(define triangle (
        (let #ph (~ $1))
        (- (* (min #ph (- 1 #ph)) 4) 1)
    )
)
triangle $x[0]
'''

# Signal de fréquence
freq = Sig(440)

# Slider de controle
freq.ctrl([SLMap(100, 2000, "lin", "value", 440, dataOnly=True)])

# Appelle le processus en lui passant un signal de fréquence
triangle = Expr(freq, proc, mul=0.4).out()

# Affichage
sc = Scope(triangle)

s.gui(locals())
