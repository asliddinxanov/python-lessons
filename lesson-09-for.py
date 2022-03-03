# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 09:21:31 2022

@author: asliddinxanov
"""
#for

cars = ['bmw','mercedes benz', 'tesla', 'audi']
for n in cars:
    print(n)
    
#----------

n = list(range(1,11))
for a in n:
    print(f"{a} square>> {a**2}")

#----------
    
n = list(range(11,100,2))
for a in n:
    print(a**3)
    
#----------

n = list(range(1,11))
n_square =[]
for a in n:
    n_square.append(a**2)
print(n)
print(n_square)

#----------

name = []
print("enter 5 names")
for a in range(5):
    name.append(input(f"{a+1}>>>"))
print(name)