# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 12:38:07 2019

@author: willfrid boris
"""

p1=str(input("PRENOM:"))
p3=str(input("NOM:"))
if(len(p1)>10 and len(p3)>10):
    s1=p1[0:3]+p1[9:12]
    s2=p3[0:2]+p3[9:12]
if(len(p1)>10 and len(p3)<10 ):
    s1=p1[0:3]+p1[9:12]
    s2=p3[0:2]+p3[6:9]
if(len(p1)<10 and len(p3)>10 ):
    s1=p1[0:3]+p1[6:9]
    s2=p3[2:5]+p3[9:12]
if(len(p1)<10 and len(p3)<10 ):
    s1=p1[0:3]+p1[6:9]
    s2=p3[0:3]+p3[6:9]
print('#####################')
print('Mashup:',s1,'',s2)
print('#####################')
