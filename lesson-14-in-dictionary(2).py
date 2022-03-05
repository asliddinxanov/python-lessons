# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 07:48:05 2022

@author: asliddinxanov
"""

#items()
#values()

car = {'model':'porsche',
        'color':'white',
        'max speed':'360km/h',
        'km':'15000km'}

for key, value in car.items():
    print(f"key : {key}")
    print(f"value : {value}\n")

#----------

prices = {
    'uzum':'26000',
    'anor':'15000',
    'nok':'12000',
    'baliq':'5000',
    'un':'25000'
    }
a = []
for b in range(5):
    a.append(input(f"{b+1}>>>"))

for food in sorted(prices):
    if food in a:
        print(f"{food.title()} {prices[food]} sum")

for food2 in a:
    if food2 not in prices:
        print(f"{food2.title()} not found")
        
#----------

#values

countris = {
    'uzbekistan':'toshkent',
    'usa':'washington d.c.',
    'russia':'moskva',
    'tadjikistan':'dushanbe',
    "kirgizistan":'bishkek',
    'qazogistan':'nursultan',
    'malayziya':'kuala-lumpur',
    'singapur':'sungapur',
    'italiya':'rim'
    }
print("Countries of the world\n")
for coun in sorted(countris):
    print(coun.upper())

print("\nCapitals of the world\n")
for cap in sorted(countris.values()):
    print(cap.title())



