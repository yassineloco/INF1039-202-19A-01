# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 14:28:47 2019

@author: kdmar
"""

print("welcome to the mashup game")

#entrer les variables

name1 = input("Entrer un nom entier(prenom nom)")
name2 = input("Entrer un autre nom entier(prenom nom)")

space = name1.find(" ")
name1_first = name1[0:space]
name1_last = name1[space+1:len(name1)]

space = name2.find("")
name2_first = name2[0:space]
name2_last = name2[space+1:len(name2)]

newname1_first = name1_first + name2_first
newname2_first = name2_first + name1_first

newname1_last = name1_last + name2_last
newname2_last = name2_last + name1_last

print(newname1_first,newname1_last)
print(newname2_first,newname2_last)
