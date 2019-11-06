# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 17:56:17 2019

@author: Nathalie
"""

print("bienvenue au mashup game")

# l'utilisateur doit entre son nom et son prenom

nom1 = str(input("entre le premier nom (FIRST LAST) : "))

# l'utilisateur a la possibilite d'entrer deux autres noms

nom2 = str(input("entre un autre nom complet (FIRST LAST): "))

# definir les premiers et dernier noms comme une variable

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

# definir la motie de chaque noms

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


# combinaison des differents noms

nouveaunom1_first = lefthalf_nom1_first.capitalize() + \
righthalf_nom2_first.lower()
nouveaunom1_last = lefthalf_nom1_last.capitalize() + \
righthalf_nom2_last.lower()

nouveaunom2_first = lefthalf_nom2_first.capitalize() + \
righthalf_nom1_first.lower()
nouveaunom2_last = lefthalf_nom2_last.capitalize() + \
righthalf_nom1_last.lower()

# afficher les noms combines premier et deuxieme noms

print("Fin! ici vous avez deux possibilitees, choississez ce que vous aimez le plus!")

print(nouveaunom1_first, nouveaunom1_last)
print(nouveaunom2_first, nouveaunom2_last)

#afficher chaque nom combine

print("vous avez termine! choississez ce que vous aimez le plus")
print(nouveaunom1_first)
print(nouveaunom1_last)
print(nouveaunom2_first)
print(nouveaunom2_last)






