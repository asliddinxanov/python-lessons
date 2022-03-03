# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 08:56:10 2022

@author: asliddinxanov
"""
#range()
#max min sum

n = list(range(0,10)) #0,1,2,3,4...n
print(n)

n = list(range(0,10,2)) #0,2,4,6...n
print(n)

#----------

n = [10,16,88,12,95,85,22,87,99,75]
a = min(n)
b = max(n)
c = sum(n)
print(a,"<",b)
print("Total = ",c)