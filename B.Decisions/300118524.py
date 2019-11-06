#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 15:18:48 2019

@author: zoureni
"""

# Opérateurs

print(3 + 2)  #Addition
print (2 * 3) #Multiplication
print(7 // 3) #Division entière
print(7 / 2) #Division
print(5 % 2) #Modulo
print(3 - 1) #Soustraction
print(3 ** 4) #Exposant

#Comparaison

print(50 > 10) #stristement superieur
print(10 < 50) #Strictement inferieur
print( 2>= 1 ) #superieur ou egal
print( 10<= 5 )# inferieur ou egal
print( 2 == 3 ) #egalité
print( 4 != 5 ) # Difference

#Menbre

print("re" in "zoureni") #menbre
print( "ut" not in "zoureni") # not menbre

#logique

print( True and True)
print(False and True)
print(True or False)
print(False or False)

 
print(3< 2 **2 and 3==3)
print ( 0!= 4 or (3/3 == 1) and (5+1) / 3 == 2)

x=2
if ( x % 2 == 0):
    print("paire")
elif ( x < 0 ):
           print("impaire négatif")
else : ("impaire positif")
    