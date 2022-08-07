# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 11:10:20 2022

@author: asliddinxaov
"""
# name = "Alex"
# old = 25
# print(name)
# print(old)

#------------

radius = 5
pi = 3.14159
face = pi * radius**2
print("Radius" , radius, "\nface of circle=", face)

a = 7_434_543_534
print(f"bizga kerak bo'ladigan son: {a}")
print("bizga kerek bo'ladigan son:", a)

# o'zgaruvchini ichiga integerni kiritsak error beradi
# chunki integer bn string qo'shilmaydi
# shuninguchun (a) o'zgarvchini str() o'tqazib olishimiz kk.
b = 'bizga kerak bo\'ladigan son: ' + str(a)
print(b)
