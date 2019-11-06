cd# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:19:11 2019

@author: 300117314
"""

#rechercher la chaine 'and; dans la variable who 

who = "me myself and I"

#imprimer la position de 'and' dans la chaine de caracter who
print (who.find ("and"))

#imprimer la chaine de caractere who 
print( len(who) )

#une autre chine de caracter
fruit = "pomme"
#imprimer le nombre de fois que le caractere 'm' apparit dans fuit I
print(  fruit.count("m"))

#imprimer la chaine de caractere 'porte' en remplacant les lettres dans fruit
print(  fruit.replace('mm' , 'ir' , 1))

#imprimer la concatenation de 'Raptors' 'vs' 'Golden State Warrios' 
concat = 'Raptors' + ' vs ' + ' Golden State Warrors'
print ( concat )

#tuple t1 vide
t1 = ()
print( t1 )

#tuple t2 une paire
t2 = ( 4, 5)
print( t2 )

# tuple t3 une paire de type different
t3 = ( 'a',2 )
print( t3 )


#tuple t4 un trio de type de types differents

t4 = ( 'a1', 2.5, False)
print (t4)
#imprimer la longueur de t4 (LENGTH)
print( len(t4) )

#imprimer la longueur d'un tuple vide
print( len( () ) )

#imprimer la valeur de t4 a l'index 2
print( t4[2] )

























