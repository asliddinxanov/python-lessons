# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 07:53:10 2022

@author: asliddinxanov
"""

#SONLAR

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

a = float(input("Enter the number>>"))
b = float(input("Enter the number>>"))
print(f"{a}+{b} =", a+b)
print(f"{a}-{b} =", a-b)
print(f"{a}x{b} =", a*b)
print(f"{a}/{b} =", a/b)

# SONLAR

# bir necha o'zgarivchiga qiymat berish

a, b, c = 1, 2, 3
print("a =", a, "b =", b, "c =", c)

# agar integerga stringni qo'shib yozish

name = "Alex"
old = 30
runn = name + " " + str(old) + "yoshda" # bu yerda old integer edi, str()metodi bn string ga aylantirdik

# O'zgaruvshini turini aniqlash

name = "Alex"
old = 30
print(type(name))
print(type(old))
# <calss 'str'> ni qaytaradi
# <calss 'int"> ni qaytaradi
