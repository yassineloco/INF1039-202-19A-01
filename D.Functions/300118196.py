#-*- coding:utf-8 -*-

#travail sur les fonctions

#Definissions de la fonction

def f(x):
    return x+1


print(f(2))

x, y = 0, 1   
while x<10:
    
    x= x+1
    x, y = x, x*2
    print(x ,'la valeur de', x ,'*', 2, 'donne', y)

