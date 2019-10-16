"""
hours to minutes:
this is a small script that converts hours in minutes

author@: martialo12
"""


def main():
    """
     hours_to_minutes program
     :return:
     """
    try:
        print("=====================================================\n")
        print("Welcome in hours_to_minutes programm:\n")
        print("=====================================================\n\n")
        hours = int(input('Please eenter the number of hours you would like to change in minutes:\n'))
        minutes = hours*60
        print("{} hours is equal to {} minutes".format(hours, minutes))
    except ValueError:
        print("!Oups... something went wrong during the program execution\n give a valid integer number!!")


if __name__ == '__main__':
    main()
