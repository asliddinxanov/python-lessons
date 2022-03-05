# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 09:12:40 2022

@author: asliddinxanov
"""

# DICTIONARY
#del/get

car = {'model':'porsche','color':'white'}
print(car['color'])

# #----------

car = {'model':'porsche','color':'white'}
car['year'] = "2022"
car['max speed'] = "380km/h"
print(car)

#----------

car = {}
car['model'] = "lexus"
car['color'] = "blue"
car['max speed'] = "360km/h"
print(car)

#----------

# del///
car = {'model':'porsche',
        'color':'white',
        'max speed':'360km/h',
        'km':'15000km'}
del car['max speed']
print(car)

#----------

#get///
dic = {'del':'delete',
        'int':'integr',
        'float':'float',
        'upper':'textni up',
        'lower':'text low',
        'title':'text title',
        'str':'string',
        'if':'agar',
        'else':'aksholda',
        'for':'format'}
a = input('Enter>>>').lower()
print(dic.get(a,"Sorry!!!"))

#----------

dic = {'del':'delete',
        'int':'integr',
        'float':'float',
        'upper':'textni up',
        'lower':'text low',
        'title':'text title',
        'str':'string',
        'if':'agar',
        'else':'aksxolda',
        'for':'format'}
a = input('Enter>>>').lower()
b = dic.get(a)
if b == None:
    print("Sorry")
else:
     print(b)