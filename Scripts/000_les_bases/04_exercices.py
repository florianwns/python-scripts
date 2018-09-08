def separator(line_break=False):
    print("\n" if line_break else "","-*-*-*-*-*-*-*-*-*")


print("##### EXERCICES ####", end="\n\n")

# Écrivez un programme qui calcule le volume d’un parallélépipède rectangle 
# dont sont fournis au départ la largeur, la hauteur et la profondeur.
def volume_parallelepipede_rectangle(largeur, hauteur, profondeur):
    return largeur*hauteur*profondeur

largeur, hauteur, profondeur = 10, 20, 30
print("Parallélépipède rectangle :")
print("=> largeur :", largeur, "cm, hauteur :", hauteur, "cm, profondeur :", profondeur, "cm")
print("=> volume ", volume_parallelepipede_rectangle(largeur, hauteur, profondeur),"cm3")
separator()


# Écrivez un programme qui affiche les 20 premiers termes 
# de la table de multiplication par 7, en signalant au passage 
# (à l’aide d’une astérisque) ceux qui sont des multiples de 3.
# Exemple: 7 14 21*28 35 42*49...
i, l = 1, 20
while i <= l:
    res = i * 7
    print(res, end=" * " if res % 3 == 0 else " ")
    i += 1
separator(True)



# Écrivez un programme qui calcule les 50 premiers termes
# de la table de multiplication par 13, 
# mais n’affiche que ceux qui sont des multiples de 7.
i, l = 1, 50
while i <= l:
    res = i * 13
    if res % 7 == 0:
        print(res, end=" ")
    i += 1
separator(True)