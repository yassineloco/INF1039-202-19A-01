# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 11:28:45 2019

@author: willfrid boris
"""

n="""
   CE PETIT PROGRAMME FAIT LA COMBINAISON DE VOS DEUX PREMIER PRENOM ET VOS DEUX PREMIER NOMS
   VEUILLEZ ENTREZ VOS DEUX PREMIERS PRENOMS ET PRENOM
   SVP
   """
print(n)
p1=str(input("PRENOM:\n"))
p2=str(input(""))
p3=str(input("NOM:\n"))
p4=str(input(""))
s1=p1[0:4]+p2[0:4]
s2=p3[0:4]+p4[0:4]
print('',s1,'',s2)
print("VOULEZ VOUS SAISIR A NOUVEAU O/N ?")
q=str(input("\n"))
if(q=='o'):
    p1=str(input("PRENOM:\n"))
    p2=str(input(""))
    p3=str(input("NOM:\n"))
    p4=str(input(""))
    s1=p1[0:4]+p2[0:4]
    s2=p3[0:4]+p4[0:4]
else:
    print("aurevoir")
    