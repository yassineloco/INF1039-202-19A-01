"""
variables

author@: martialo12
"""


def main():
    """
     python utilise type inference
     :return:
     """
    # Ma variable
    x = 1
    print(2 * x)

    # Integer
    x = 4
    print(2 * x)
    if (x == 4):
        print('x = 4')
    else:
        print('on ne sait pas')

    # string
    a = 'x = 4'
    print(a)


if __name__ == '__main__':
    main()
