#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Les modules

Comment importer et utiliser un module
"""
import sys
import mes_modules.fibonacci as fibo

# on pourrait aussi écrire :
# from mes_modules import fibonacci as fibo

# on pourrai aussi importer tout les modules du package
# nécessite le fichier __init__.py
# from mes_modules import *

# nom du module
print(fibo.__name__)

# documentation du module
print(fibo.__doc__)

# appel d'une fonction du module
res = fibo.fib(50)
print(res)

# affiche les dossiers de modules de python
# va cherche l'info dans la variable shell PYTHONPATH
for path in sys.path:
    print(path)


# les version compilés des modules sont conservés
# au format .pyc dans le dossier __pycache__


# listes des noms définis dans le module
print(dir(fibo))

# dir() liste les noms actuellement définis
# mais dir() ne liste ni les fonctions primitives,
# ni les variables internes.
# Si vous voulez les lister, elles sont définies dans le module builtins :
print(dir())
