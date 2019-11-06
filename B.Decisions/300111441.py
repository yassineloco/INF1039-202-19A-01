# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 15:23:45 2019

@author: skofo
"""

# operateurs table 14.2 p 123

print(3 +2) # Addition
print(2 * 3) # Multiplication
print(7 // 3) #Divisin entiere
print(7 / 2) # Division
print(5 % 2) # Modulo
print(5 - 2) # soustraction
print(2 ** 8) # Exposant

# Comparaison

print(50 > 10) # Strictement superieur
print(2 >= 1) # Superieur ou egal
print(8 < 2) # strictement inferieur
print(10 <= 5) # Inferieur ou egal
print(2 == 3) # Egalite
print(4 != 5) # Difference

#Membre

print("br" in "Brince")
print("co" not in "korlings") # Not membre

#Logique
print(True and True)
print(False and True)
print(True or False)
print(False or False)

#Combinaison
print(3> 2 ** 3 and 3 == 3)
print(0 != 4 or (3 / 3 == 1 and (5 + 1)/3 ==2)) 
print("a" in "code" or "b" in "python" and len ("programme")==7)

x=2
if (x % 2 == 0):
   print("pair") 
elif (x < 0):
    print ("impair negatif")
else :
    print ("impair positif")    