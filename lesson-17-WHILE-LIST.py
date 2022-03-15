# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 05:43:10 2022

@author: asliddinxanov
"""
# WHILE LIST

print("Do'stlar ro'yxatini.")
ism = []
n = 1

while True:
    a = f'{n}chi ismni kiriting>>>'
    b = input(a)
    ism.append(b)
    c = input('yana ism qo\'shazizmi?(xa/yo\'q)')
    n += 1
    if c != 'xa':
        break
    
print('Do\'stlar ro\'yxati:') 
for b in ism:
    print(b.upper())
# =============================================================================
# 
# =============================================================================

d = {}
i = True

while i:
    ism = input("ismni kiriting>>>")
    yosh = input(f'{ism.title()}ning yoshini kiriting>>>')
    d[ism] = int(yosh)
    
    j = input('yana bormi?(xa/yo\'q)')
    if j == 'yo\'q':
        i = False

for a, b in d.items():
    print(f'{a.title()}nin yoshi{b}da!')
# =============================================================================
# 
cars = ['lacettu', 'nexia', 'tico', 'nexia', 'audi', 'malibu', 'nexia']
while 'nexia' in cars:
    cars.remove('nexia')
print(cars)
# 
# =============================================================================
cars = ['lacettu', 'nexia', 'tico', 'audi', 'malibu']
car_speed = {}
while cars:
    car = cars.pop()
    speed = input(f'{car} speed >>>')
    car_speed[car] = int(speed)
for a,b in car_speed.items():
    print(f'{a.title()}s speed {b}km/h')
# =============================================================================
# 
# =============================================================================
a = []
i = True
while i:
    b = input('maxsulot nomini kiriting>>>')
    a.append(b)
    t = input('yana bormi?(xa/yo\'q)')
    if t == 'yo\'q':
        i = False
print('Ro\'yxatalr:')
for r in a:
    print(r.upper())
# =============================================================================
# 
# =============================================================================
buyurtmalar = ['olma','anjir','uzum','qovun']
mahsulotlar = {'olma':20000,
                'shaftoli':25000,
                'tarvuz':18000,
                'uzum':22000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"{buyurtma} topilmdi!!!")