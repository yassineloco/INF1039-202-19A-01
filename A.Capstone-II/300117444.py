# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 11:27:47 2019

@author: idirAbib

"""

# Se programme nous permet de taper 2prenom et nom different et 
# de cree un nouveau nom et prenom a partir des premier .

#Entrer un nom et un prenom
NomPrenom1 = input('Veuillez entrer un nom et un prenom:')
#Entrer un 2eme nom et 2eme un prenom
NomPrenom2 = input('Veuillez entrer le 2eme nom et prenom:')



#choisir les variables ou les  caracteres pour afficher le nom1

Nom1 = (NomPrenom1[1:5] + NomPrenom2[5:10] )

#choisir les variables ou les  caracteres pour afficher le nom1

Nom2 = (NomPrenom1[5:9] + NomPrenom2[2:8])


#afficher les les nouveau noms

print (Nom1) #Affiche le nom N1
print(Nom2)#Affiche le nom N2
