"""Les instruction"""

# test de l'instruction if elif et else
a = 0
if a > 0:
    print("a est positif")
elif a < 0:
    print("a est négatif")
else:
    print("a est egale à 0")

# Affichage de x, x^2, x^3 sur les 10 premier chiffres
while a <= 10:
    print(a, a**2, a**3)            # Attention : python ne suporte pas 
    a += 1                          # l'opérateur d'incrementation => a++ 

# Suite de Fibonnaci sur les 20 premiers élements
a, b, i, l = 1, 1, 1, 20
while i <= l:                                   # l'opérateur ternaire s'écrit :
    print(b, end=":" if i < l else "\n")        # => a if condition else b
    a, b, i = b, a+b, i+1                 

# Affichage des 20 premiers multiples de 7
i, mul, l = 1, 7, 20
while i <= l:
    print(i * 7, end=":" if i < l else "\n")
    i += 1

# Conversion euros => dollars canadien
euro, conv, limit = 1, 1.65, 16384
while euro <= limit:
    # on utilise format pour formatter les nombres
    print("{:,} euros (s) = {:,.2f} dollar (s)".format(euro,euro*conv)) 
    euro *= 2

# Multiplication par 3 du dernier élement sur les 12 premiers élements
i, b, n = 1, 1, 12
while i <= n:
    print(b, end=":" if i < n else "\n")
    i, b, = i+1, b*3
