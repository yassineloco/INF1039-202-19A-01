# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 14:23:32 2019

@author: zacks
"""
# Operateurs table 14.2 p 123 

print (3 + 2) #addition
print (2 + 3) #multiplication
print (7 // 3) #division entiere
print (5 / 2) #division normale
print ( 5 % 2) #modulo
print (5 - 2) #soustraction
print (2 ** 8) #exposant

# Comparaison

print (50 > 10) #strictement superieur
print (10 >= 5)  #superieur ou egal
print (8 < 2) #strictement inferieur 
print (10 <= 10) #strictement inferieur ou egal 
print (2 == 3) #egalite
print ( 4 != 5) #difference

# mEMBRE
print ("Br" in "Brice") #membre
print ("Za" not in "Mouloud" ) #non logique

# Logique
print (True and True)
print (False and True)
print (True or False)
print (False or False)

# Combinaison
print ( 3 < 2 ** 3 and 3 == 3)
print ( 0 != 4 or (3/3 == 1 and (5 + 1 ) / 3 ==2))

print ("a" in "code" or "b" in "python" and len("programme") == 7)

x=2
if (x %  2 == 0):
    print ("pair")
elif (x < 0):
        print("impair negatif")
else : ("impair positif") 

















