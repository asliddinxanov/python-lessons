# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 09:46:48 2022

@author: asliddinxanov
"""
# if-else

cars = ['mercedes benz', 'bmw', 'volvo', 'general motors', 'tesla', 'audi']
for a in cars:
    if a == 'bmw':
        print(a.upper())
    else:
        print(a.title())
        
#----------

cars = ['mercedes benz', 'bmw', 'volvo', 'general motors', 'tesla', 'audi']
for a in cars:
    if a != 'bmw':
        print(a.title())
    else:
        print(a.upper())
        
#----------

a = float(input('a = '))
b = float(input('b = '))
if a > b:
    print('\na katta')
if b > a:
    print('\nb katta')
else:
    print("\na = b")

#----------

n = int(input('How old are you?'))
if n >= 18:
    print('Welcome')
else:
    print("Sorry!!! you not 18+")
    
#----------

login = input("Yangi login kiriting \n>>>")
if len(login) <= 4:
    print("Login 4ta xarfdan ko'p bo'lishi kerak")
else:
    print("OKKEY")

#----------

n = input("新しいIDを入力してください\>>>")
if len(n) <= 4:
        print("IDが4文字多くてならなければなりません!!")
        if n != n.title():
            print("最初の文字を大文字にしてください!!")
else:
    print("ようこそ")   

#----------

n = float(input("Siz son kiriting biz sizga ildizini chiqarib beramiz\n>>>"))
print(n**(1/2)) if n >= 0 else print("Musbat son kiriting")

#----------

n = int(input('How old are you?>>>'))
if n <= 7:
    print("Sizga kirish mumkin emas!")
elif n <= 65:
    print("Marxamat!")
else :
    print("Sizni yoshingiz juda katta ekan!!!")

#----------

n = int(input("How old are you?>>>"))
if n <= 7:
    price = '5000sum'
elif n <= 65:
    price ='15000sum'
else :
    price = '0sum'
print(price)

#----------

