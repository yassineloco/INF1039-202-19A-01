# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:20:16 2019

@author: K-D Marie Auriane
"""

#Rechercher la chaine 'and' dans la variable who

who = "moi moi-meme et Je"

#Imprimer la position de 'et' dans la chaine de caractere who 
print('prob 1')
print (who.find("et"))


#Imprimer la longueur de la chaine de caractere who
print('prob 2')
print( len(who) )

# une autre chaine de caractere
fruit = "Pomme"

#Imprimer le nombre de fois que le caractere 'm' apparait dans fruit
print('prob 3')
print(fruit.count('m'))

#Imprimer la chaine de caractere 'Poire' en remplacant les lettres dans fruit
print('prob 4')
print(fruit.replace("mm","ir"))

#Imprimer la concatenation de 'Raptors' 'vs' 'Golden State Warriors'
concat = 'Raptors' + 'vs' + 'Golden State Warriors'
print( concat )

#Tuple t1 vide
t1 = ()
print(t1)

#Tuple t2 une paire
t2 = (4,5)
print( t2 )

#Tuple t3 une paire de meme type different
t3 = ('a',2)
print( t3 )

#Tuple t4 un trio de types differents 
t4 =('a1', 2,5, False)
print (t4)

#Imprimer la longueur de t4
print( len(t4) )

#Imprimer la longueur d,un tuple vide 
print( len( () ))

#Imprimer la valeur de t4 a l'index 2
print(t4[2])