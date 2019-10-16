"""
author@: martialo12
"""


def main():
    """
     strings
     :return:
     """
    # Rechercher la le charactère 'e' dans la vriable who
    who = "io io stesso e io"
    position = who.find('e')

    # imprimer la longueur de la chaine de charactère who
    print(len(who))

    print('e se trouve à la position: {}'.format(position))

    # une autre chaine de charactère
    fruit = "pomme"

    # imprimer le nombre de fois que le charactèrère 'm' apparait das fruit
    print(fruit.count('m'))

    # imprimer la chaine decharactère 'poire' en remplaçant les lettres das fruit
    print(fruit.replace('mm', 'ir'))

    # Imprimer la concatenation de 'Raptors' et 'Golden State Warriors' '
    concat = 'Raptors' + 'vs' + 'Golden State Warriors'
    print(concat)

    # tuples t1 vide
    t1 = ()
    print(t1)

    # Tuple t2 est une paire
    t2 = (4, 5)
    print(t2)

    # tuple t3 une paire de type différent

    t3 = ('a', 2)
    print(t3)

    # tuple t4 un tio de types différents
    t4 = ('a1', 2.5, False)

    print(t4)

    # imprimer la longueur de t4
    print(len(t4))

    # imprimer longueur d'un tuple vide
    print(len(()))

    # imprimer la valeur de t4 à l'index
    print(t4[2])


if __name__ == '__main__':
    main()

