#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Les annotations de fonctions

les annotations sont stockés dans l'attribut __annotations__
à titre de documentation
et n'ont aucun effet sur l'éxécution du code
"""



def command_meal(count: int = 0, meal: str = "", table: int = None) -> str:
    if table is None :
        return "Please, give us the number of your table"
    res = "Hey Chief, i need {0} {1} for the table number {2}"
    return res.format(count, meal, table)


print(command_meal.__annotations__)
print(command_meal(3, "Burger"))
print(command_meal(3, "Burger", 19))
