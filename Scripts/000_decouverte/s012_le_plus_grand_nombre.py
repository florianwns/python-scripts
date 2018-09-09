"""Affiche le plus grand nombre d'une liste

On demande à l'utilisatuer de renseigner plusieurs nombres
On calcule et affiche le nombre le plus grand
"""

print("Veuillez entrer plusieurs nombres séparés par des virgules : ")
ch = input()
t = list(eval(ch))  # equivaut à list((1, 2, 3, 4, ...)) 
                    # => (1, 2, 3, 4) est un tuple
print("Le nombre le plus grand dans",t,"est :",max(t))