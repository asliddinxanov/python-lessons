# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 10:06:53 2022

@author: XanovsPC
"""

# LAMBDA

# aylananing uzunligini hisoblabsh
import math

a = lambda pi, r : 2*pi*r
print(a(math.pi, 10))

kv = lambda x, y : x**y
print(kv(2, 3))

def daraja(n):
    return lambda x : x**n
kv = daraja(2)
ku = daraja(3)

print(f"4-ning kvadrati {kv(4)}, "
      f"4-ning kubi {ku(4)} ga teng")

# =============================================================================
# map
# =============================================================================

from math import sqrt

sonlar = list(range(11))
sqr = list(map(sqrt, sonlar))
print(sonlar)
print(sqr)

def daraja2(x):
    return x*x
print(list(map(daraja2,sonlar)))

kv = list(map(lambda x: x*x, sonlar))
print(kv)

a = [1,3,4]
b = [4,3,1]

axb = list(map(lambda x,y : x*y, a,b))
print(axb)

# =============================================================================
# filter
# =============================================================================

import random as r

a = r.sample(range(100),10)
kv_filter = list(filter(lambda x: x%2==0, a))
print(a)
print(kv_filter)

mevalar = ["olma","anor","nok","o'rik","qovun","olcha"]
o = "o" #mevalar listidan o harfidan boshlanadigan mevani olib chiqaradi
meva_o = list(filter(lambda x: x.startswith(o),mevalar))
print(meva_o)

a = list(filter(lambda x: (x.startswith("a") and x.endswith("a")), mevalar))
print(a)