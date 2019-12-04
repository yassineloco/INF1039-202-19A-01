# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:10:26 2019

@author: skofo
"""
import math

def f( x):
    return x + 1
a = 1
while a < 10:
    print(math.sqrt(f(a)))
    a= a + 1