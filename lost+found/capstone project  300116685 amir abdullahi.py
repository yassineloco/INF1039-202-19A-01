# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 13:11:38 2019

@author: -capstone project : name mashup 
"""

# ""storing the first and last names in variables ""

# Affiche une variable ayant pour nom Amir abdullahi
  
nom1 = str(input("entre le premier nom (first and last):" ) )
nom2= str (input ("entre un autre nom famille (first and last):") )
 
 #operer les variables 
space=nom1.find(" ")
nom1_first = nom1[0 : space ]
nom1_last = nom1[space+1 : len (nom1)]
space = nom2.find("")
nom2_first = nom2[0: space]
nom2_last = nom2[space+1 : len (nom2)]
 
print (nom1_first)
print (nom1_last)
print (nom2_first)
print (nom2_last)


 