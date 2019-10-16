"""
variables

author@: martialo12
"""


def main():
    """
     python utilise type inference
     :return:
     """

    # creer une variable s contenant la chaine 'ma chaine'
    s = 'ma chaine'
    print(s)

    # Afficher le premier caractere
    print(s[0])

    # Afficher le caractere 'i'
    print(s[6])

    # afficher la chaine de caractere 'ai' dans la chaine 'ma chaine'
    print(s[5:7:1])

    # afficher la chaine de caractere 'an' dans la chaine 'ma chaine'
    print(s[5:8:2])


if __name__ == '__main__':
    main()
