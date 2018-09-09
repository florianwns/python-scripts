# Déterminer si une année (dont le millésime est introduit par l’utilisateur) 
# est bissextile ou non. Une année A est bissextile si A est divisible par 4. 
# Elle ne l’est cependant pas si A est un multiple de 100,
# à moins que A ne soit multiple de 400.

annee = int(input("Merci de renseigner une année : "))
bissextile = annee % 400 == 0 or annee % 4 == 0 and annee % 100
print(annee, "est" if bissextile else "n'est pas", "une année bissextile")
