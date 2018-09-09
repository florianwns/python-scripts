"""Quel est donc ce triangle ???

Demander à l’utilisateur d’entrer trois longueurs AB, AC, BC. 
À l’aide de ces trois longueurs, déterminer s’il est possible de construire un triangle. 
Déterminer ensuite si ce triangle est rectangle, isocèle, équilatéral ou quelconque. 
Attention : un triangle rectangle peut être isocèle.
Si BC² = AB² +AC² alors le triangle est rectange en A
"""

def safe_int(value):
    try:
        return int(value)
    except:
        return 0

ab = safe_int(input("Longueur de AB : "))
ac = safe_int(input("Longueur de AC : "))
bc = safe_int(input("Longueur de BC : "))
t = sorted([ab, ac, bc]) # tri les longueurs de la plus petite à la plus grande

if not ab or not ac or not bc:
    print("ABC n'est pas un triangle")
    exit()

triangle = "quelconque"
if t[2] == t[1] and t[1] == t[0] and t[0] == t[2]:
    triangle = "equilatéral"
elif t[2] == t[1] or t[1] == t[0] :
    triangle = "rectangle isocèle" if t[2]**2 == t[0]**2 + t[1]**2 else "isocèle"
elif t[2]**2 == t[0]**2 + t[1]**2:
    triangle = "rectangle"

print("ABC de longueurs",t,"est un triangle " + triangle)
