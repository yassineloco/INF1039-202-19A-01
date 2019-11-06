# -*- *-coding utf-_8  -*-

try:

    def parité():

        print('bonjour et bienvenue \n')
        nombre = int(input('veuillez inserér un nombre: '))

        if nombre > 0:
            print("c'est nombre positif\n")
        else:
            print("c'est nombre negatif\n")

        if nombre % 2 == 0:
            print("de plus, il s'agit d'un nombre paire\n")
        else:
            print ("de plus, il s'agit d'un nombre impaire\n")

    parité()

except ValueError:
    print("merci d'inserer un entier valide\n")



