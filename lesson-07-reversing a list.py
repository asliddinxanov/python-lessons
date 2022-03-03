# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 08:44:18 2022

@author: asliddinxanov
"""
# Reserving a list
#.sort
#sorted
#.reverse()
#len()
#indeks

cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
cars.sort()
print(cars)

#reverse=True
cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
cars.sort(reverse=True)
print(cars)

#----------

cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
print(sorted(cars))
print(cars)

#----------

cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
cars.reverse()
print(cars)

#----------

cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
print(len(cars))

#----------

cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
print(cars[1:3]) # >>'mercedes benz', 'volvo'
print(cars[:3])  # >>'bmw','mercedes benz', 'volvo'
print(cars[1:])  # >>'volvo', 'general motors', 'tesla', 'audi'
print(cars[1])   # >>'mercedes benz'
print(cars[3])   # >>'general motors'