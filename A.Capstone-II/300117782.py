# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 16:49:49 2019

@author: User
"""

print('bienvenu dans mon jeu')




def get_random(character):

        prename = str(input('veuillez saisir votre prénom: '))
        postname = str(input('veuillez entrer par la suite votre nom usuel: '))

        space = prename.find(" ")                               # mettre un espace entre les differents carectères de prename
        prename_first = prename[0:space]                        # limiter la liste postname jusqu'à l'espace
        prename_last = prename[space+1:len(prename)]            # prendre tout les caractères

        space = postname.find(" ")
        postname_fist = postname[0:space]
        postname_last = postname[space+1:len(postname)]


        prename_first = prename_first[0:4] + postname_last[0:3]
        prename_last = prename_last [0:3] + postname_fist[0:4]
        postname_fist = prename_last[0:4] + postname_last[0:4]
        postname_last = prename_first[0:4] + postname_fist[0:3]

        print(prename_first)
        print(prename_last)
        print(postname_fist)
        print(postname_last)





get_random(0)

print('Merci, Bonne journée')