import math

def separator(line_break=False):
    print("\n" if line_break else "","-*-*-*-*-*-*-*-*-*")

print("##### EXERCICES ####", end="\n\n")

# 5.1 Écrivez un programme qui convertisse en radians 
# un angle fourni au départ en degrés, minutes, secondes.
# 1 degré = 60 min , 1 mn = 60 sec 

def deg_to_rad(deg=0,min=0,sec=0):
    return (deg + min/60 + sec/3600) * (math.pi/180)


# 5.2 Écrivez un programme qui convertisse en degrés, minutes, secondes 
# un angle fourni au départ en radians.
def rad_to_deg(rad=0):
    deg = rad * 180/math.pi         # conversion radian degree
    min = deg%1 * 60
    sec = min%1 * 60
    return "{0:d}°{1:d}'{2:d}\"".format(int(deg), int(min), round(sec))

deg, min, sec = 40, 7, 60
rad = deg_to_rad(deg, min, sec)
print(rad, "radians => ", rad_to_deg(rad))


# 5.3 Écrivez un programme qui convertisse en degrés Celsius une température 
# exprimée au départ en degrés Fahrenheit, ou l’inverse.
# La formule de conversion est : Fahrenheit = Celsius x 1.8 + 32
def fahrenheit_to_celcius(temperature):
    return (temperature - 32) / 1.8

def celcius_to_fahrenheit(temperature):
    return temperature * 1.8 + 32

deg = 39.800001
fah = celcius_to_fahrenheit(deg)
print(fah, "°F => ", fahrenheit_to_celcius(fah),"°C")


# 5.5 Une légende de l’Inde ancienne raconte que le jeu d’échecs a été inventé par un vieux sage, 
# que son roi voulut remercier en lui affirmant qu’il lui accorderait 
# n’importe quel cadeau en récompense. Le vieux sage demanda qu’on lui fournisse 
# simplement un peu de riz pour ses vieux jours, et plus précisément un nombre de grains 
# de riz suffisant pour que l’on puisse en déposer 1 seul sur la première case du jeu 
# qu’il venait d’inventer, deux sur la suivante, quatre sur la troisième, 
# et ainsi de suite jusqu’à la 64e case.
# Écrivez un programme Python qui affiche le nombre de grains 
# à déposer sur chacune des 64 cases du jeu. C
# 
# Calculez ce nombre de deux manières :
# • le nombre exact de grains (nombre entier) ;
# • le nombre de grains en notation scientifique (nombre réel) .

i, g, total = 1, 1, 0   # g = 1.0 pour la notation en nombre réel 
while i <= 64:
    total += g
    print(i, g)
    i, g = i+1, g*2

print("Nombre total de grains de riz : ", total)
print("Nombre total de grains de riz : ", 2**64-1) # Autre façon plus rapide => 2^n - 1
