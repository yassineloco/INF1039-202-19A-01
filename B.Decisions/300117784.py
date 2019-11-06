# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 13:35:28 2019

@author: Bertrand
"""
#Operateurs table pages 14.2

print(3 + 2) # Addition
print(2 * 3) # Multiplication 
print(7 // 3) # Division entiere 
print(7 / 2)# Division normale 
print(5 % 2) # Modulo 

#Comparaison

print( 50 > 10 ) #Strictement superieur
print(2 >= 1)# superieure ou egale 
print(8 < 2)#strictement inferieur 
print( 10 <=5 ) # Inferieur ou egale
print( 4 != 5 )# Different 

#Membre
print("tr" in "Bertrand")
print("Co" not in "Korlings")

#Logique

print(True and True)
print(False and True)
print(True or True)
print(False or False)

#Combinaison

print( 3 < 2 ** 3 and 3 == 3)
print( 0 != 4 or (3 / 3 == 1 and ( 5 + 1) / 3 == 2))

print("a" in "code" or "b" in "python" and len("programme") == 7)

#if

x=2

if (x % 2 == 0):
    print ("pair")
elif (x < 0 ):
    print ("impaire negatif")

else : print("impair positif")