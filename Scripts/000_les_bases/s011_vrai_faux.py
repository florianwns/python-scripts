"""Test des valeurs d'égalité

Tester les variables à vide est plus rapide que de tester
une variable avec une autre
ex :
    => if a != "": 
est plus lent que 
    => if a: 
"""

t = ["", "test", 0, 1, -1, 0.0, 0.1, True, False, [], [1], {}, {2,3}, object, None]
for value in t:
    print(value,"=> Vrai" if value else "=> Faux", type(value))