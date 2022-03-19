# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 08:16:42 2022

@author: asliddinxanov
"""

# MODULES

"""
modules in python web site
https://docs.python.org/3/library/math.html#module-math

"""

# math

import math

n = 25
print(math.sqrt(n))
print(pow(2,2))
print(math.pi) #...

# =============================================================================
# random(x), randint(x), choice(x)
# =============================================================================

import random as r

n = r.randint(0,50)
print(n)

m = list(range(0,50,10))
print(m)
print(r.choice(m))

names = ['ali', 'vali', 'gani', 'sheri']
a = r.choice(names)
print(a)
print(r.choice(a))

# =============================================================================
# shuffle(x)
# =============================================================================

n = list(range(0,10))
r.shuffle(n)
print(n)