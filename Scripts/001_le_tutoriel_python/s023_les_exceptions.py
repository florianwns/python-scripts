#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Les exceptions

Les exceptions sont utilisées pour la gestion des erreurs d'éxécution
Exceptions natives : https://docs.python.org/fr/3/library/exceptions.html
"""

# le code ci-dessous déclenche une exception
try:
    raise Exception("On a un petit souci, Captain' !")
except Exception as e:
    print(type(e))
    print(e.args)
    print("Une exception a été déclenchée :", e)
except:
    print("Une erreur s'est produite mais aucune exception n'a été attrapée")
else:
    print("le code contenu dans 'try' n'a pas levé d'exception, on continue")
finally:    # finally peut être utile pour libérer des ressources
    print("le code contenu dans 'finally' s'éxécutera de toute façon")


# division par 0, ce qui va déclencher, une exception de type ZeroDivisionError
try:
    x = 1/0
except ZeroDivisionError as e:
    print("Erreur :", e)
