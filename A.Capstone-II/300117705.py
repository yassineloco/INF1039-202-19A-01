# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 23:35:01 2019

@author: corlings
"""

# welcome to the mashup program

# ce programme permet de melanger deux prenoms et deux noms

# afficher une variable ayant pour nom'lauren bacale'
name1 = 'Marie Aurianne'

# afficher une variable ayant pour nom'richard simone'
name2 ='Archange Corlings'

# entrer le nom de la variable
name1 = input('entrer prenom et nom: ')

# entrer le nom de la variable
name2 = input('entrer prenom et nom: ')

# entrer premiere moitie du prenom name1 + deuxieme moitie du prenom name2
n1 = (name1[2:3] + name2[4:7])

# entrer premiere moitie du nom name1 + deuxieme moitie du nom name2
n2 = (name1[0:3] + name2[4:9])

# entrer premiere moitie du prenom de name2 + deuxieme moitie du prenom name1
n3 = (name2[0:3] + name1[3:6])

# entrer premiere moitie du nom name2 + deuxieme moitie du nom name2
n4 = (name2[8:11] + name1[10:14])

# imprimer en premier lieu noms et prenoms melanges separemment
print(n1)
print(n2)
print(n3)
print(n4)

# imprimer nom et prenom dans une meme ligne
print( n1,n2)
print(n3,n4)
