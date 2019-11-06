# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 15:22:01 2019

@author: User
"""

3 + 2

print(3 + 2) # Addition
print(2 * 3) # multiplication
print(7 // 3) # Division entiere
print(7 / 2) # Division
print(5 % 2) # Modulo
print(5 - 2) # soustraction
print(2 ** 8) # Exposant

# Comparaison
print(50 > 10) # strictement superieur
print(2 >= 1) # superieur ou egal
print(8 < 2) # strictement inferieur
print(10 <= 5) # inferieur ou egal
print(2 == 3) # egalite
print(4 != 5) # difference

print("Ha" in "Hassana") # membre
print("co" not in "korlings") # not membre

# Logique
print( True and True)
print( False and True)
print(True and False)
print( False and False)

# combination

print( 0 != 4 or(3/3 ==1 and(5 + 1)/3 ==2))
print("a" in "code" or "b" in "python" and len("programnme")==7)



X=2
if (X % 2==0):
    print("pair")
elif (X < 0):

    print("impair negatif")
else: ("impair positif")