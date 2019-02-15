"""Les constantes de PYO

source : http://ajaxsoundstudio.com/pyodoc/api/constants.html
"""
from pyo import *

# version de PYO
print(PYO_VERSION)

# True si precision 64bits sinon False 32bits
print(USE_DOUBLE)

# True si PYO a été compilé avec des classes externes
print(WITH_EXTERNALS)

# Chemin du dossier son de PYO (situé dans les packages de python)
print(SNDS_PATH)
