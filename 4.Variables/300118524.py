#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 13:54:55 2019

@author: zoureni
"""

who = 'me myself and me'
#imprimer la position de 'and' dans la chaine de caractere who

print( who.find("et"))

#imprimer la longueur de la chaine de caractère who

print( len(who))

fruit= 'pomme'

#imprimer le nombre de fois de caractère 'm' apparaît dans le fruit

print(fruit.count('m'))

#imprimer la chaîne de caractère 'poire' en remplacant les lettres dans fruit

print(fruit.replace('mm','ir'))

#imprimer la concatenation de 'Raptors' 'vs' 'Golden State Warriors'

concat = 'Raptors' + ' vs ' + 'Golden State Warriors'

print( concat)

#Tuple t1 vide
t1 = ()
print( t1 )

#Tuple t2 une paire de meme type
t2 = (4 , 5)
print( t2 )

#Tuple t3 une paire de type différent
t3 = ('a', 2)
print( t3 )

#Tuple t4 un trio de type différents
t4 = ('a1', 2.5, False )
print( t4 )

#imprimer la longueur de t4
print(len( t4 ))

#imprimer la longueur d'un tuple vide
print(len(()))

#imprimer la valeur de t4 à l'index 2
print([2])
