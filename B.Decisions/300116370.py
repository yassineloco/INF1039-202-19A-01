# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 15:31:33 2019

@author: khali
"""



print(2+3)   # addition
print(5*5)   # multiplication
print(4//4)  # divsion entiere
print(5 % 3)  # modulo
print(2 ** 5) # exposant

# comparaison
print(50 > 15) # strictement superieur
print(2 >= 1) # superieur ou egal

print(5 < 2)  # strictement inferieur
print(7 <= 4) # inferieur ou egal
print(5 == 6) # egalite
print(3 != 6) # difference

print('ca'in 'carla')
print('jo' not in 'paul')
 
# logique
print(True  and True)
print(False  and True)
print(True  and False )
print(False  and False )    
      

# combinaison
print(3 < 2**3 and 3==3)
print(0 != 4 or (3/3 == 1 and (5+1) / 3 ==2))
print('a' in 'code' or 'b' in 'python' and len('programm') == 7)

x = 2
if (x % 2 == 0):
    print('pair')
elif(x<0): 
    print('impair negatif')
else: 
    print('impair positif')
    
    
    
    
    

