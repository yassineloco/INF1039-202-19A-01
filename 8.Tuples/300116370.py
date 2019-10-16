# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:21:05 2019

@author: khali
"""

#rechercher la chaine anddans la variable who
who = "me myself and i"
print(who.find("and"))

# imprimer la chaine de caractere who

print('prob 2') 
print(len(who))

# une autre chaine de caractere
fruit = "pomme"

# imprimer le nombre de fois que le caractere "m "apparait dans fruit
print('prob 3')
print(fruit.count('m'))

# imprimer la chaine de caractere'poire' remplacant les lettres dans fruit
print(fruit.replace('mm','ir'))
        
# imprimer la concatenation de 'raptors' 'vs' 'golden state warriors'        
concat = 'raptors' + 'vs' + 'golden state warriors'        
print(concat)

# tuple t1 vide
t1 = ()
print(t1)  

# tuple t2 une paire
t2 = (4, 5) 
print(t2)

#tuple t3 une paire de type different
t3 =('a', 2)
print(t3)

# tuple t4  un trio de type differents
t4 = ('a1', 2.5, False )
print(t4)  

# imprimer la longueur de t4
print(len(t4))  

# imprimer la longueur d'un tuple vide
print(len())

# imprimer la valeur de t4 a l'index
print( t4[2])

print( t4[2])
