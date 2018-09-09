# Écrivez un programme qui permette d’encoder des valeurs numérique dans une liste. 
# Ce programme devrait fonctionner en boucle, 
# l’utilisateur étant invité à entrer sans cesse de nouvelles valeurs, 
# jusqu’à ce qu’il décide de terminer en frappant <Enter> en guise d’entrée. 
# Le programme se terminerait alors par l’affichage de la liste. 

t = []
while True:
    try:
        x = input("Veuillez entrer une valeur : ")
        if x == "":
            break
        t.append(int(x))
    except:
        continue

print(t)    
    
