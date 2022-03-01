# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 11:51:39 2022

@author: asliddinxanov
"""
#upper() and lower()

name = "James"
surname = "Bond"
name_surname = f"{name} {surname}"
print(name_surname.upper())

print(name_surname.lower())

#title() and #capitalize()

name_surname = "james bond"
print(name_surname.title())

name_surname = "james bond"
print(name_surname.capitalize())

#strip(), rstrip() and lstrip() methods

a = "   is   "
print("Time"+ a +" money")
print("Time"+ a.strip()+" money")
print("Time"+ a.rstrip()+" money")
print("Time"+ a.lstrip()+" money")

#input 

name = input("What's your name? >>>")
surname = input("What's your surname? >>>")
name_surname = f"{name.title()} {surname.title()}"
print(f"Hello {name_surname}")





