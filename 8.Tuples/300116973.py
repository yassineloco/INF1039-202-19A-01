# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:38:04 2019

@author: dell
"""
#rechercher la chaine 'and' dans la variable who

who = "me myself and I"
print ('prob 1')
print(who.find('and'))

# imprimer la position de 'I' dans la chaine de caractere who

print(who.find("I"))

# imprimer la longueur de la chaine de caractere who
print ('prob 2')
print( len(who) )

#  une autre chaine de caractere
fruit = "pomme"

# imprimer le nombre de fois que le caractere 'm' apparait dans fruit

print(fruit.count('m'))
print ('prob 3')
#Imprimer la chaine de caractere 'poire' en remplacant les lettres dans fruit

print(fruit.replace('mm', 'ir'))

#Imprimer la concatenation de 'Raptors' 'vs' 'golden state warriors'

concat = 'Raptors' + 'vs'  + 'Golden State Warriors'
print(concat)

# Tuple t1 vide

t1 = ()
print( t1 )

# Tuple t2 une paire de meme types

t2 = (4, 5)
print(t2)

#Tuple t3 une paire de types differents
t3 = ('a', 2)
print( t3 )


# Tuple t4 un trio de types differents
t4 = ('a1', 2.5, False)
print( t4 )

# Imprimer la longueur de t4 (Length)
print ( len(t4) )

# Imprimer la longueur d'un tuple vide
print(len(()))

# Imprimer la valeur de t4 a l'index 2

print( t4[2])





