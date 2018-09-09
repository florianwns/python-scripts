"""Les listes"""

# les élements d'une liste peuvent être variés
liste = ["Bonjour", 3, 4.0, object]
liste[1] += 2
liste.append("steve")
print(liste)
print("Longueur => ",len(liste))

print(liste[1:4])   # prend les élements 1, 2 et 3 en paratant de 0


# Écrivez un petit programme qui crée une nouvelle liste t3. 
# Celle-ci devra contenir tous les éléments des deux listes en les alternant, 
# de telle manière que chaque nom de mois soit suivi du nombre de jours correspondant :

t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
      'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
t3 = []
for i in range(0, len(t1)):
    t3.append(t2[i])
    t3.append(t1[i])
print(t3)

# Écrivez un programme qui affiche « proprement » tous les éléments d’une liste. 
print(" ".join(t2))


# Écrivez un programme qui recherche le plus grand élément présent dans une liste donnée. 
# Par exemple, si on l’appliquait à la liste [32, 5, 12, 8, 3, 75, 2, 15] 
# ce programme devrait afficher : 75
t = [32, 5, 12, 8, 3, 75, 2, 15]
print("Max : ", max(t))

# Ecrivez un programme qui analyse un par un tous les éléments d’une liste de nombres 
# pour générer deux nouvelles listes. 
# L’une contiendra seulement les nombres pairs de la liste initiale, 
# et l’autre les nombres impairs. 

odd  = list(filter(lambda x: x % 2 == 0, t))
even = list(filter(lambda x: x % 2 == 1, t))
print("Pair : ", odd)
print("Impair : ", even)

# Écrivez un programme qui analyse un par un tous les éléments 
# d’une liste de mots (par exemple : ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']) 
# pour générer deux nouvelles listes. 
# L’une contiendra les mots comportant moins de 6 caractères, 
# l’autre les mots comportant 6 caractères ou davantage.

t = ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']
t1 = list(filter(lambda x: len(x) < 6, t))
t2 = list(filter(lambda x: len(x) >= 6, t))
print(t1, t2)

