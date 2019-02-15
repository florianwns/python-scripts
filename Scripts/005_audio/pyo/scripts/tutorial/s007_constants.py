"""Les constantes de PYO
"""
from pyo import *

# version de PYO
print(PYO_VERSION)

# True si la précision des doubles est de 64bits
# sinon False si la précision des doubles est de 32bits
print(USE_DOUBLE)

# True si PYO a été compilé avec des classes externes
print(WITH_EXTERNALS)

# Chemin du dossier son de PYO (situé dans les packages de python)
print(SNDS_PATH)
