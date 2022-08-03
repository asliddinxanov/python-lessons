# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 08:17:46 2022

@author: asliddinxanov
"""

#list

a = ['APPLE', 'orange', 'pear', 'peach', 'banana']
print(a[0])
print(a[-1])

#----------

#.title()
#.upper()
#.lower()

print(a[0].upper())
print(a[1].title())
print(a[0].lower())

#----------

#.append()
#.insert()
#del
#.remove(n)
#.pop()

a = ['APPLE', 'orange', 'pear', 'peach', 'banana']
a.append("lemon")
print(a)

a = ['APPLE', 'orange', 'pear', 'peach', 'banana']
a.insert(0, "lemon")
print(a)

a = ['APPLE', 'orange', 'pear', 'peach', 'banana']
del a[1]
print(a)

a = ['APPLE', 'orange', 'pear', 'peach', 'banana']
a.remove("pear")
print(a)

a = ['APPLE', 'orange', 'pear', 'peach', 'banana']
b = a.pop(0)
print(a)
print(b)







