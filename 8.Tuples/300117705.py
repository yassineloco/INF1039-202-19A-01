# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:47:46 2019

@author: corlings
"""
# recherche la chaine 'and' dans la variable who
who = "mwen menm e Mwen"
 
print (who.find("e"))

# imprimer la longueur de la chaine de caractere who
print(len(who))

# une autre chaine de caractere

fruit = "pomme"

# imprimer le nombre de fois que le caractere 'm' apparait dans fruit
print(fruit.count('m'))

 
 # imprimer la chaine 'poire' en remplacant les lettres dans fruit
print(fruit.replace("mm","ir" ))

# Imprimer la contatenation de 'Raptors' 'vs' 'Golden state worrior'
concat = 'Raptors' + ' vs ' + 'Golden State Warriors'
print( concat )

# Tuple t2 une paire de meme types
t2 = ( 4, 5 )
print( t2 )

# Tuple t3 un paire type differents
t3 = ( 'a', 2 )

# Tuple t4 un trio de type differents
t4 = ( 'a1', 2.5, False )
print( t4 )

# Imprimer la longueur de t4 (length)
print( len(t4) )

# Imprimer la longueur d'un tuple vide
print( len(()))

# Imprimer la valeur de t4 a l'index 2
print( t4[2] )
