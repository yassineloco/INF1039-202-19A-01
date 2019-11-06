# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 15:19:15 2019

@author: 300098957
"""

# Operateurs Table 14.2 p 123

print(3 + 2) # Addition
print(2 * 3) # Multiplication
print(7 // 3) # Division entiere
print(7 / 2) # Division
print(5 % 2) # Modulo
print(5 - 2) # Soustraction
print(2 ** 8) # Exposant

# Comparaison 

print(50 > 10) # Strictement superieur 
print( 2 >= 1 ) # Superieur ou egal
print( 8 < 2 ) # Strictement inferieur
print( 10 <= 5 )  # Inferieur ou egal
print( 2 == 3 ) # Egalite
print( 4 != 5 ) # Difference

# Membre

print("Br" in "Brice") # membre
print("Co" not in "Korlings") # not membre

# Logique
print( True and True)
print( False and True)
print( True or False)
print( False or False)

# Combinaison
print( 3 < 2 ** 3 and 3 == 3)
print( 0 != 4 or (3/3 == 1 and (5 + 1) / 3 == 2) )

x = -2
if (x % 2 == 0):
    print("pair")
elif (x < 0):
    print("impair negatif")
else:
    print("impair positif")
    
    

