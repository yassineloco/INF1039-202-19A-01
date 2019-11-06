# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 17:02:00 2019

@author: Jeremie
"""


# operation
print(3 + 2) # addition
print(2 * 3) # multiplication
print(7 // 3) # division entiere
print(7 / 2) # division
print(5 % 2) # modulo
print(5 - 2) # soustraction
print(2 ** 8) # exposant

# comparaison
print( 50 > 10 )
print( 2 >= 1 )
print( 8 < 2 )
print( 10 <= 5 )
print( 2 == 3)
print( 4 != 5)

# menbers
print("co" in "corlings")
print("ko" not in "corlings")

# logique

print( True and True )
print( False and True )
print( True or False )
print( False or False )

# combinaison
print( 0 != 4 or (3 / 3 == 1 and (5 + 1)/3 == 2))


print("a" in "code" or "b" in "python" and len("programme") ==7)

x = 2
if (x % 2 == 0):
    print("pair")
elif ( x < 0 ):
    print("impair negatif")
else:
    print("impair negatif")