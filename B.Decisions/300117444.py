# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 18:09:15 2019

@author: idirAbib
"""


print(6 + 3) # Addition
print(8 * 3) # multiplication
print(5 // 5)# division entiere
print(12 / 2)#Division
print(10 % 2)# modulo
print(9 - 5)# soustraction
print(3 ** 8)# exposant

# comparaison

print(26 > 16)# strictement superieur
print(4 >= 1)# superieur ou egal
print(9 < 2)# strictement inferieur
print(10 <= 5)#Inferieur ou egale
print(2 == 2)#egalite
print(4 != 5)#difference

#member
print("com" in "commisaire")  #membre
print("to"not in "toronto")  #not member

#logique

print (True and True)
print(False and True)
print (True or False)
print(False or False)

#combinaison
print( 4 < 2 ** 3 and 3 == 3)
print(0 != 4 or (3/3 == 1 and (5 + 1) / 3 == 2) )

print ('z' in 'code' or 'b' in 'python'and len("programm") ==7)

x = 4

if (x % 5 == 0):
    print("pair")
elif (x < 0 ) :
    print("Chiffre impaire negatif")
else : ("Chiffre impaire positif")
