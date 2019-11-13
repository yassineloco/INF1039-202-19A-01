# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 15:38:17 2019

@author: khali
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 15:24:38 2019

@author: khali
"""

# welcome to the mashup program

# ce programme permet de melanger deux prenoms et deux noms

# afficher une variable ayant pour nom'lauren bacale'
name1 = 'lauren bacale'

# afficher une variable ayant pour nom'richard simone'
name2 ='richard simone'

# entrer le nom de la variable
name1 = input('entrer prenom et nom: ')

# entrer le nom de la variable
name2 = input('entrer prenom et nom: ')

# entrer premiere moitie du prenom name1 + deuxieme moitie du prenom name2
r1 = (name1[0:3] + name2[3:7])

# entrer premiere moitie du nom name1 + deuxieme moitie du nom name2
r2 = (name1[7:10] + name2[11:14])

# entrer premiere moitie du prenom de name2 + deuxieme moitie du prenom name1
r3 = (name2[0:3] + name1[3:6])

# entrer premiere moitie du nom name2 + deuxieme moitie du nom name2
r4 = (name2[8:11] + name1[10:14])

# imprimer en premier lieu noms et prenoms melanges separemment
print(r1)
print(r2)
print(r3)
print(r4)

# imprimer nom et prenom dans une meme ligne
print( r1,r2)
print(r3,r4)