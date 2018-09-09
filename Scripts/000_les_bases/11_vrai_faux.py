
# Test des valeur d'égalité
t = ["", "test", 0, 1, -1, 0.0, 0.1, True, False, [], [1], {}, {2,3}, object, None]
for value in t:
    print(value,"=> Vrai" if value else "=> Faux", type(value))