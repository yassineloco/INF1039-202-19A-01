#-*- coding:utf-8 -*-

#travail sur les fonctions

# @author: martialo12

import math

def puissance_2(x):
    return x**2

print(puissance_2(2))

x = 1   
while x<10:
    x= x+1
    y = puissance_2(x)
    # determiner l'ensemble des valeurs obtenu à la suite de l'itération de puissance_2(x)
    print('la racine carre de {} est : {}'.format(y, math.sqrt(y)))
