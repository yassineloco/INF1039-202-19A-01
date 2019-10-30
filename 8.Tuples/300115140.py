# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:20:48 2019

@author: zacks
"""

#rechercher la chaine dans la variable who
who = "me myself and I"

who.find ("and")
who = "Ich Meine und Du"
#imprimer la position de und dans la chaine
print ( who.find("und"))

#imprimer la longeur de la chaine de caractere


#une autre chaine de caractere

fruit = "Pomme"

#imprimer le nombre de fois que le caractere "m" apparait dans fruit

print ('prob 1')
print( fruit.count('m'))

#imprimer la chaine de caratere 'Poire' en remplacant lettre dans fruit
print ('prob 2')


print( fruit.replace('mm', 'ir'))

#imprimer la concatenation de 'Raptors' 'vs' 'Golden Sates Warriors'
concat = 'Raptors' + ' vs ' + 'Golden Sates Warriors'
print ( concat )

#Tuple t1 vide
t1 = ()
print (t1)

# Tuple t2 uen paire de meme type

t2 = ( 4,5 )
print ( t2 )

# Tuple t3 une paire de type different

t3 = ( 'a',2 )
print (t3)

#Tuple t4 avec 3 types differents

t4 = ('b2', 2.5, False )
print (t4)

#imprimer la longeur de t4

print ( len(t4) )

#imprimer la longeur d'un tuple vide
print( len(()))

#imprimer la valeur de t4 à Lindex 2
print ( t4 [2] )

















