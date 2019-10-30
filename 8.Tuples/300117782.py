# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:21:07 2019

@author: User
"""

# Rechercher la chaine 'and' dans la variable who
who = "moi  moi-meme et JE"

# Imprimer la position de 'et'dans la chaine de caractere
print( 'prob1' )
print (who.find("et"))
# Imprimer la longueur de la chaine de caractere who

print( 'prob2' )
print(len(who))

# Une autre chaine de caractere

Fruit ="Pome"

# Imprimer le nombre de fois que le caractere 'm' apparait dans fruit
print( Fruit.count( 'm'))


# Imprimer la chaine de caractere 'poire en remplacant les lettres dans fruit
print( Fruit.replace('mm','ir'))

# Imprimer le nombre de fois que le caractere 'm' apparait dans fruit
print( 'prob 3')
Concat = 'Rapports' + 'vs' + ' Golden State Warriors'
print ( Concat ) 

# Tuple t1 vide
t1 = ( )
print( t1 )
# Tuple t2 une paire 
t2 = (4 ,5)
print( t2 )
# Tuple t3 une paire de type different
t3 =( 'a' , 2)
print( t3 )
# Tuple t4 un trio de types different
t4 = ('a1' , 2.5, False )
print( t4 )
# Imprimer la longueur de t4 (length)
print( len(t4) )
#Imprimer la longueur d,un tuple vide
print( len(()))
# Imprimer la valeur de t4 a l'index 2
print( t4[2] )