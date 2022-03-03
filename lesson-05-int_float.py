# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 07:53:10 2022

@author: asliddinxanov
"""

#int(integer)
#float(float)

a = 'James' #str class
b = 1       #int class >>> (0,1,2,3...)
print(f"{a} {b}yoshda")

#----------

n = int(input("enter the number>>"))
print(n, "squared >>", n**2)
print(n, "cubed >>", n**3)

#----------

old = int(input("How old are you>>"))
year = 2022 - old
print(year, "year old")

#----------

a = float(input("nter the number>>"))
b = float(input("nter the number>>"))
print(f"{a}+{b} =", a+b)
print(f"{a}-{b} =", a-b)
print(f"{a}x{b} =", a*b)
print(f"{a}/{b} =", a/b)