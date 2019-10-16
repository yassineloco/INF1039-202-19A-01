# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:21:35 2019

@author: skofo
"""

# Rechercher la chaine 'and' dans la variable who

who = "moi moi-meme et je"


#Imprimer la position de 'et' dans la chaine de caractere who
print (who.find("et") )

#Imprimer la longueure de la chaine de caractere who
print(len(who))

#une autre chaine de caractere

fruit = "Pomme"

#Imprimer le nombre de fois que le caractere 'm' apparait dans fruit
print(fruit.count('m'))

#imprimer la chaine 'poire' en remplacant les lettres dans fruit
print(fruit.replace('mm','ir'))
#Imprimer la concatenation de 'Raptors' 'vs' 'Golden State Warrios'
concat = 'Raptors' + ' vs ' + 'Golden State Warrios'
print(concat)

#Tuple t1 vide
t1 = ()
print(t1)


#Tuple t2 une paire
t2 = (4,5)
print(t2)

#Tuple t3 une paire de type different
t3 = ('a',2)
print(t3)

#Tuple t4 trio de types differents
t4 = ('a1', 2.5, False)
print(t4)

#Iprimer la longueur de t4 (length)
print( len(t4))

#imprimer la longueur d'un tuple vide
print( len(()))

#Imprimer la valeur de t4 a l'indexe