# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 15:23:39 2019

@author: 3300116973
"""

print(3 + 2) # Addition
print(2 * 3) # multiplication
print(3 // 3)# division entiere
print(7 / 2)#Division
print(5 % 2)# modulo
print(5 - 2)# soustraction
print(2 ** 8)# exposant

# comparaison

print(50 > 10)# strictement superieur
print(2 >= 1)# superieur ou egal
print(8 < 2)# strictement inferieur
print(10 <= 5)#
print(2 == 3)#egalite
print(4 != 5)#difference

#member
print("br" in "bracelet")#membre
print("co"not in "corrola")#not member

#logique

print (True and True)
print(False and True)
print (True or False)
print(False or False)

#combinaison
print( 3 < 2 ** 3 and 3 == 3)
print(0 != 4 or (3/3 == 1 and (5 + 1) / 3 == 2) )

print ('a' in 'code' or 'b' in 'python'and len("programm") ==7)

x = 4

if (x % 4 == 0):
    print("pair")
elif (x < 0 ) :
    print("impair nefatif")
else : ("impair positif")
