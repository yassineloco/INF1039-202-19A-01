# -*- coding: utf-8 -*-

"""
Created on Tue Nov  5 09:31:05 2019

@author: willfrid boris
"""
n="""
   CE PETIT PROGRAMME FAIT LA COMBINAISON DE VOTRE PREMIER ET DERNIER NOM
   VEUILLEZ ENTREZ VOTRE PREMIER ET DERNIER NOM
   SVP
   """
print(n)
p1=str(input("NOM:\n"))
p2=str(input("PRENOM:\n"))
s=p1[0:3]+p2[2:3]
print(s)
print("VOULEZ VOUS SAISIR A NOUVEAU O/N ?")
q=str(input("\n"))
if(q=='o'):
    p1=str(input("NOM:\n"))
    p2=str(input("PRENOM:\n"))
    s=p1[1:3]+p2[1:3]
    print(s)
else:
    print("aurevoir")
    
    
    






