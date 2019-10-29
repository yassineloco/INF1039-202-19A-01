# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 21:47:52 2019

@author: dell
"""
# convertir les minutes en heures et minutes en utilisant une partir decimal

minutes_to_convert  =  123

hours_decimal  = minutes_to_convert/60

hours_part  =  int(hours_decimal)

minutes_decimal =  hours_decimal-hours_part

minutes_part  =  round(minutes_decimal*60)

print ("Hours")

print (hours_part)

print("Minutes")

print (minutes_part)

# convertir les minutes en heures et minutes en utilisant le reste

minutes_to_convert  = 123

hours_decimal = minutes_to_convert/60

hours_part  =  minutes_to_convert%60

print("Hours")

print (hours_part)

print ("Minutes")

print (minutes_part)



    
