#-*- coding:utf-8 -*-

#travail sur les fonctions

#Definissions de la fonction

import math

def f(x):
    return x*2

print(f(1),'\n')

print("l'ensemble des racines de f(x)\n")

x, y = 0, 1   
while x<10:
    x= x+1
    y = f(x)
    
#determiner l'ensemble des valeurs obtenu à la suite de l'itération de f(x)
    print("la valeur de ", x,'*', 2, 'donne comme racine carré',math.sqrt(f(x)))

