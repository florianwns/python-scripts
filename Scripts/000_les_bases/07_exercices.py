import math

# 5.6 Écrivez un script qui détermine si une chaîne contient ou non le caractère « e ».
txt = "Bonjour mon petit oiseau"
print("'{}' contient la lettre e => {}".format(txt, txt.find("e") > 0))

# 5.7 Écrivez un script qui compte le nombre d’occurrences du caractère « e » dans une chaîne.
occ, count = "e", 0
for char in txt:
    if char == occ:                     # Autre écriture : 
        count += 1                      # count += 1 if char == occ else 0

print("Il y a {} '{}' dans '{}'".format(count, occ, txt))


# 5.8 Écrivez un script qui recopie une chaîne (dans une nouvelle variable), 
# en insérant des astérisques entre les caractères.
# Ainsi par exemple, « gaston » devra devenir « g*a*s*t*o*n »
txt, copy, i = "gaston", "", 0
while i < len(txt):
    copy += "*"+txt[i] if i > 0 else txt[i]
    i += 1
print(copy)

# 5.9 Écrivez un script qui recopie une chaîne (dans une nouvelle variable) en l’inversant. 
# Ainsi par exemple, « zorglub » deviendra « bulgroz ».
txt, copy = "zorglub", ""
i = len(txt) - 1        # on commence par la fin 
while i >= 0:
    copy += txt[i]
    i -= 1
print(txt, "=>", copy)

# 5.10 En partant de l’exercice précédent, écrivez un script qui détermine 
# si une chaîne de caractères donnée est un palindrome 
# (c’est-à-dire une chaîne qui peut se lire indifféremment dans les deux sens), 
# comme par exemple « radar » ou « s.o.s ».
def is_palindrome(txt=""):
    i, l = 0, len(txt)
    while i < l:
        if txt[i] != txt[-i-1]:
            return False
        i += 1
    return True

print("'S.0.S' est un palindrome => ", is_palindrome("S.0.S"))

