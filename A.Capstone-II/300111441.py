# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 20:57:57 2019

@author: skofo
"""

print("Bienvenue dans le jeu de melange")

#Entrez votre variable

nom1 = input("Inserer votre nom complet(prenom nom)")
nom2 = input("Inserer le second nom complet(prenom nom)")

space = nom1.find(" ")
nom1_first = nom1[0:space]
nom1_last = nom1[space+1:len(nom1)]

space = nom2.find("")
nom2_first = nom2[0:space]
nom2_last = nom2[space+1:len(nom2)]

nouvelnom1_first = nom1_first + nom2_first
nouvelnom2_first = nom2_first + nom1_first

nouvelnom1_last = nom1_last + nom2_last
nouvelnom2_last = nom2_last + nom1_last

#Imprimez nouvelnom1 et nouvelnom2

print(nouvelnom1_first,nouvelnom1_last)
print(nouvelnom2_first,nouvelnom2_last)