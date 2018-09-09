"""Les variables"""

a = b = 7
c, d = 2, 3
prenom = "frédéric"
pi = 3.14159

print(a, b, c, d, prenom, pi)
print("type(a) => ", type(a))
print("type(\"Bonjour\") == type(0) => ", type("Bonjour") == type(0))

a, b, c = 3, 5, 4
x = a - b//c
print(x, "=>", type(x))

a, b = 5.6, 2
y = 3*a + b/0.2
print(y, "=>", type(y))

a, b = b, a     # echange de valeur sans passer par une variable c
print(a, b)
