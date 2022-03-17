# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 07:57:18 2022

@author: asliddinxanov
"""
# FUNCTIONS

def hello(a):
    print(f'Hello {a}')
hello('World')

# =============================================================================
# 
# =============================================================================

a = int(input('enter number: '))
def kvadrat(a):
    print(a**2)
kvadrat(a)

# =============================================================================
# 
# =============================================================================

a = int(input('enter number: '))
def kvadrat(a):
    if a%2 == 0:
        print('juft son')
    elif a%2 !=0:
        print('toq son')
kvadrat(a)

# =============================================================================
# 
# =============================================================================

a = int(input('enter number: '))
b = int(input('enter number: '))
def kvadrat(a, b):
    if a > b:
        print(f'{a} katta')
    elif a < b:
        print(f'{b} katta')
    else:
        print('Sonlar teng!!!')
kvadrat(a, b)

# =============================================================================
# 
# =============================================================================

def bolish(a):
    for n in range(2,11):
        if not a%n:
            print(f'{a} {n}ga qoldiqsiz bo\'linadi!!!')
            
a = int(input('enter number: '))
bolish(a)

# =============================================================================
# 
# =============================================================================

def avto_info(com, model, color, php, year, price = None):
    avto = {
        'kampaniya': com,
        'modeli': model,
        'rangi': color,
        'karobkasi': php,
        'yili': year,
        'narhi': price
        }
    return avto
avto1 = avto_info('GM','Malibu','oq','avtomat','2021')
avto2 = avto_info('GM','Nexia','qora','mexanika','2006',6000)
avtolar = [avto1,avto2]

print('Bozordadi mashinalar ro\'yxati:')
for a in avtolar:
    if a['narhi']:
        price = a['narhi']
    else:
        price = 'Nomalum'
    print(f"{a['modeli']}, rangi {a['rangi']}, {a['karobkasi']}"
          f" karobka, {a['yili']}yilda ishlab chiqarilgan, narxi = {price}")

# =============================================================================
# 
# =============================================================================

def oraliq(min, max):
    n = []
    while min<max:
        n.append(min)
        min += 1
    return n

print(oraliq(0,10))
print(oraliq(10,21))

# =============================================================================
# 
# =============================================================================

def mijoz_info(ism, fam ,tyil, tjoy, email= '', tel= None):
    mijoz = {
        'ism': ism,
        'familiya': fam,
        'tyili': tyil,
        'yosh': 2022-tyil,
        'tjoyi': tjoy,
        'email': email,
        'telefon': tel
        }
    return mijoz

print('Mijoz xaqida ro\'yxat: ')
mijozlar = []
while True:
    ism = input('Ismini kiriting: ')
    fam =  input('Familiyasini kiriting: ')
    tyil = int(input('Tug\'ilgan yilini kiriting: '))
    tjoy =  input('Yashash joyini kiriting: ')
    email = input('Email: ')
    tel = input('Tel raqamini kiriting: ')
    mijozlar.append(mijoz_info(ism, fam, tyil, tjoy, email, tel))
    j = input('yana qo\'shasizmi?(yes/no)')
    if j == 'no':
        break

print("\nMijozlar ro'yxati")
for a in mijozlar:
    print(f"{a['yosh']}yoshli {a['ism'].title()} {a['familiya'].title()} "
          f"{a['tjoyi']}da dunyoga kelgan, "
          f"Email: {a['email']}, TEL= {a['telefon']}")

# =============================================================================
# 
# =============================================================================

def max_find(x, y, z):
    max = x
    if y >= max:
        max = y
    if z >= max:
        max = z
    return max

x = int(input('enter (x) number: '))
y = int(input('enter (y) number: '))
z = int(input('enter (z) number: '))
print(max_find(x, y, z))

# =============================================================================
# 
# =============================================================================

def tub_son_find(min, max):
    tub_son = []
    for n in range(min, max+1):
        tub = True
        if (n==1):
            tub = False
        elif (n==2):
            tub = True
        else:
            for a in range(2,n):
                if (n%a==0):
                    tub = False
        if tub:
            tub_son.append(n)
    return tub_son

min = int(input('boshlanish sonni kiriting: '))
max = int(input('tugash sonni kiriting: '))
print(tub_son_find(min, max))

# =============================================================================
# FIBANACCI
# =============================================================================

def fibanacci(n):
    a = []
    for x in range(n):
        if x == 0 or x == 1:
            a.append(1)
        else:
            a.append(a[x-1] + a[x-2])
    return a

print('FIBANCCI')
n = int(input('nechta fibanachi son kerakligini kiriting: '))
print(fibanacci(n))