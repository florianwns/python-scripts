
def incr(a):
    return a + 1    # ici on incrémente une variable locale, passé en paramètre

def a_incr():
    global a        # on utilise le mot clé 'global' pour accéder à la variable
    a += 1


a = 0
a_incr()            # a incrémente a dans la fonction en utilisant le mot clé 'global'
a = incr(a)         # on réaffecte à a la valeur retourné par incr
print(a)            # a vaut 2
incr(a)             # ici a ne varie pas, car il n'y pas d'affectation
print(a)            # a vaut toujours 2


