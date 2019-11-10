# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:29:53 2019

@author: USER
"""
# rechercher la chaine 'and' dans la variable who

who = "me myself and me"

# imprimer la position de 'et' dans la chaine who 

print(who.find('and'))

# imprimer la longueur de la chaine de caractère who
print ( len (who) )

# une autre chaine de caractere

fruit = "pomme"
# imprimer le nombre de fois que le caractère 'm ' apparait dans fruit

print(fruit.count('m'))

# imprimer la chaine de caractere 'poire' en remplacant les letres dans fruit
print (fruit.replace('mm', 'ir', )) 
# imprimer concatenation de 'Raptors' 'vs' 'Golden states warriors'
concat = 'Raptors' + ' vs ' + 'Golden states warriors'
print (concat)  

# tuple t2 une paire de même type
t2 = (4,5)
print(t2)

# tuple t3 une paire de type differents
t3 = ('a', 45)
print(t3)
#tuple t4 un trio de type differents
t4 = ('Q1', 2.5, False)
print (t4)
# la longueur de t4
print(len(t4))

# imprimer la longueur d'un tuple vide
print (len(()))
# imprimer la valeur de t4 à l'index 2

print(t4[2])  
