# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:13:29 2019

@author: idira
"""
# Rechercher la chain e 'and ' dans la variable who
who ="moi moi-meme et JE "
#Imprimer la position de 'et' dans la chaine de caracter who
print(who.find("e"))

# imprimer la longueur de la chaine de caractere who
print(len(who))

fruit = "pomme"
#imprimer le nombre de fois que le caractere 'm' apparait dans le fruit
print(fruit.count('m'))

#imprimer la chaine de caractere 'poire' en remplacant les lettres dans fruit
print(fruit.replace('mm','ir',))
 
#Imprimer la concatenation de 'Raptors' 'vs' 'Golden State Warriors
concat = 'Raptors ' +   'vs '+ 'Golden State Warriors'
print (concat)

#tuple t1 vide
t1 = ()
print( t1)

#tuple t2 une paire
t2 = ( 4 , 5)
print (t2)

# Tuple t3 une paire de type different
t3 = ('a',2)
print (t3)

#Tuple t4 un trio de type different
t4= ('a2',2.5,False)
print (t4)

#Imprimer la longueur de t4 ( length)
print (len(t4))
#Imprimer la longueur d'in tuple vide
print( len(())) # les parenthese pcq ces vide

#Imprimer la valeur de t4 a l'index 2
print (t4[2])

#
       
