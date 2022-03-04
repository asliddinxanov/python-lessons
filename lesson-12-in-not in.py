# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 08:11:48 2022

@author: asliddinxanov
"""

# IN / NOT IN

menu = ['manti','somsa','shashli','osh']
a = input("Enter yor order >>>")
if a.lower() in menu:
    print("Order accepted")
else:
    print("Order not found")

# ----------

menu = ['manti','somsa','shashli','osh']
a = input("Enter yor order >>>")
if a.lower() not in menu:
    print("Order not found")
else:
    print("Order accepted")

#----------

menu = ['manti','somsa','shashlik','osh']
a = ['osh','shashlik','gosht','manti']
for order in a:
    if order in menu:
        print(f"{order} is accepted")
    else:
        print(f"{order} not fond in menu!")
        
#----------

menu = ['manti','somsa','shashlik','osh']
a = ['osh','shashlik','gosht','manti']
if a:
    for order in a:
        if order in menu:
            print(f"{order} is accepted")
        else:
            print(f"{order} not fond!")
else:
     print("Your list is empty")
    
#----------

n = int(input("Enter even number>>>"))
if (n % 2) == 0 :
    print("OKEY")
else:
    print("This not even number!!!")

#----------

n = int(input("Enter even number>>>"))
if n % 2:
    print("This not even number!!!")
else:
    print("OKEY")

#----------
# order algorithm

menu = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
        'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
zakaz = []
for a in range(5):
    zakaz.append(input(f"{a+1}) enter your food>>>"))
    
accepted = []
not_found = []

for ovqat in zakaz:
    if ovqat in menu:
        accepted.append(ovqat)
    else:
        not_found.append(ovqat)

if not_found:
    print("This orders not found")
    for ovqat in not_found:
        print(ovqat)
else:
    print("All orders accepted")

#----------

login = ['ali','vali','nilu','moli','quli']
a = input("Enter your new login>>>")

if a.lower() in login:
    print("This login is available")
else:
    print(f"Welcome!!! {a.title()}")

#----------

users = ['alisher1983','aziza','yasina' 'umar']

login = input("Enter your new login>>>" )

if login in users:
    print('This login is available!')
else:
    print("Welcome!!!")
    
#----------

son = int(input("Istalgan 5dan katta bo'lgan butun son kiriting>>>"))

for n in range(2,son):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
