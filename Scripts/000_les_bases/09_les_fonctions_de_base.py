from math import sqrt

# print permet d'afficher n'importe quel nombre de valeurs passés en arguments
print("Bonjour", 5, 4.0, [3,"hey"], end ="\n*\n", sep="-")

# input permet la saisie au clavier
x = ""
while True:
    try:
        x = int(input("Entrez un chiffre compris entre 0 et 10 : "))
        break
    except:
        continue

# permet de tester le type d'une variable 
if isinstance(x,int):       # type(x) is int
    print("Racine carré de ", x, "=>", sqrt(x))


#len => longueur d'une chaine
