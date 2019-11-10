# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 18:47:11 2019

@author: zacks
"""

print("bienvenue au mashup game")

# Entrer deux noms et prenoms

nom1 = str(input("entre le premier nom (FIRST LAST) : "))
nom2 = str(input("entre un autre nom complet (FIRST LAST): "))

# etablir les varaibles

space = nom1.find(" ")

nom1_first = nom1 [0:space]

nom1_last = nom1 [space+1:len(nom1)]

space = nom2.find(" ")

nom2_first = nom2 [0:space]

nom2_last = nom2[space+1:len(nom2)]

print(nom1_first)
print(nom1_last)
print(nom2_first)
print(nom2_last)

# moitie des noms

len_nom1_first = len(nom1_first)

len_nom2_first = len(nom2_first)

len_nom1_last = len(nom2_last)

len_nom2_last = len(nom2_last)


index_nom1_first = int(len_nom1_first/2)

index_nom2_first = int(len_nom2_first/2)

index_nom1_last = int(len_nom1_last/2)

index_nom2_last = int(len_nom2_last/2)


lefthalf_nom1_first = nom1_first [0:index_nom1_first]

righthalf_nom1_first = nom1_first [index_nom1_first:len_nom1_first]

lefthalf_nom2_first = nom2_first [0:index_nom2_first]

righthalf_nom2_first = nom2_first [index_nom2_first:len_nom2_first]


lefthalf_nom1_last = nom1_first [0:index_nom1_last]

righthalf_nom1_last = nom1_first [index_nom1_last:len_nom1_first]

lefthalf_nom2_last = nom2_first [0:index_nom2_last]

righthalf_nom2_last = nom2_first [index_nom2_last:len_nom2_first]


# mash up des noms

nouveaunom1_first = lefthalf_nom1_first.capitalize() + \
righthalf_nom2_first.lower()
nouveaunom1_last = lefthalf_nom1_last.capitalize() + \
righthalf_nom2_last.lower()

nouveaunom2_first = lefthalf_nom2_first.capitalize() + \
righthalf_nom1_first.lower()
nouveaunom2_last = lefthalf_nom2_last.capitalize() + \
righthalf_nom1_last.lower()

# afficher les noms combines premier et deuxieme noms

print("C'est fini! choississez celui que préférez")

print(nouveaunom1_first, nouveaunom1_last)
print(nouveaunom2_first, nouveaunom2_last)

#afficher chaque nom combine

print("C'est fini! choississez celui que préférez")
print(nouveaunom1_first)
print(nouveaunom1_last)
print(nouveaunom2_first)
print(nouveaunom2_last)