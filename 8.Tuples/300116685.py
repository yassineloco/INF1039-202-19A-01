# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:23:41 2019

@author: Amir
"""

print('hello')
#tuple t1 vide
t1 = ()
print ( t1 )
# tuple t2 une paire  de meme type
t2 = (4, 5)
print ( t2 )

#tuple t3 une paire de type different 
t3 = ('a', '2'  )
print( t3 ) 
#tuple  t4 un trio de type de types differents 
t4 = ('a1', 2.5, False) 
print ( t4 ) 
# imprimer la longueur de t4 (length)
print (len(t4) ) 
# imprimer la longueur d'un tuple vide 
print (len(())) 
#imprimer la valeur de t4 a l'index 2 
print( t4 [2] )
