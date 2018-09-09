import sys

# Les entiers sont codés sur 32 bits compris entre -2147483648 et +2147483647 
# (enfin cette limite dépend de votre processeur 32 ou 64 bits)
# Cependant en Python, un entier peut dépasser ces limitations,
# les opérations seront du coup plus longue car python devra traiter 
# plus d'opérations dont le réencodage des données pour un même calcul .
# le type 'long int' n'a plus besoin d'exister

# Affichage des 50 premières puissances de 2
i, p = 1, 1
while i <= 50:
    p = 2**i
    print("2^{0:d} => {1:d} =>".format(i, p), type(p))
    i += 1


# Déclaration et initialisation de nb à virgules flottantes
a, b, c, d, e, f, g = 3.14, 10., .0001, 1e100, 3.14e-10, 3.14e+309, 2.225e-409
print(a, b, c, d, e, f, g)

print("Float min value => ", sys.float_info.min)
print("Float max value => ", sys.float_info.max)





# les chaines de caractères 
chaine = 'n\'est pas étrange ?'
print(chaine)

# Attention au nombre d'espaces en début de ligne sur les longues chaine de caractères
chaine = "  Sous un grand ciel gris, dans une grande plaine poudreuse,\
 sans chemins, sans gazon, sans un chardon, sans une ortie,\
 je rencontrai plusieurs hommes qui marchaient courbés.\n\n\
  Chacun d'eux portait sur son dos une énorme Chimère,\
 aussi lourde qu'un sac de farine ou de charbon, ou le fourniment d'un fantassin romain."

print(chaine)

# avec 3 guillemets, plus besoin de saut de ligne, ou de \ pour les doubles quotes
chaine = """
  Mais la monstrueuse bête n'était épas un poids inerte ;
 au contraire, elle enveloppait et opprimait l'homme de ses muscles élastiques
 et puissants ; elle s'agrafait avec ses deux vastes griffes à la poitrine de sa monture ;
 et sa tête fabuleuse surmontait le front de l'homme, comme un de ces casques horribles par
 lesquels les anciens guerriers espéraient ajouter à la terreur de l'ennemi.
"""
print(chaine)

texte, i = "Bonjour en chinois se dit '你好'", 0
while i < len(texte):
    print(texte[i])
    i += 1
