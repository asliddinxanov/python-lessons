# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 08:49:17 2022

@author: asliddinxanov
"""



# a = input("Ismingizni kiriting : ")
# b = f'Salom {a.title()}. Yoshingizni kiriting : '
# yosh = int(input(b))

# WHILE

# print('Kiritilgan sonni kvadratuni qaytaruvchi dastur!!!')
# a = 'Sonni kiriting,'
# a += ('to\'xtash uchun \'exit\' deb yozing>>>')
# b = ''
# while b != 'exit':
#     b = input(a)
#     if b != 'exit':
#         print(float(b)**2)

# a = 'sonni kiriting,'
# a += "to\'xtatish uchun \'exit\'deb yozing>>>"

# c = True
# while c:
#     b = input(a)
#     if a == 'exit':
#         c = False
#     else:
#         print(float(b)**2)
# print("ovari")

# =============================================================================
# BREAK
# =============================================================================

# print('Kvadratlovchi dastur')
# a = "sonni kiriting,"
# a+= "to'xtash uchun 'exit'ni yozing\n>>>"

# while True:
#     b = input(a)
#     if b == 'exit':
#         break
#     else:
#         print(float(b)**2)

# =============================================================================
# CONTINUE
# =============================================================================

# n = list(range(1,11))
# for a in n:
#     if a == 5:
#         continue
#     else:
#         print(f'{a} ning kvadrati = {a**2}')

# n = 0
# while n < 10:
#     n += 1
#     if n%2!=0:
#         continue
#     else:
#         print(n)

# =============================================================================

# =============================================================================

# a = "Yoshingizni kiriting,chiqish uchun 'quit' yoki 'exit' deb yozing>>>"
# while True:
#     b = input(a)
#     if b == "exit" or b == "quit":
#         break
#     yosh = int(b)
    
#     if yosh<7:
#         price = 2000
#     elif 7 <= yosh < 18:
#         price = 3000
#     elif 18 <= yosh < 65:
#         price = 10000
#     else: price = 0
    
#     if price == 0:
#         print('Sizga chipta bepul')
#     else:
#         print(f'chipta narxi {price}sum')

# =============================================================================

# =============================================================================

a = "ildizlovchi dastur"
a += "Mubat son kiriting"
a += "o'chirish uchun 'exit' yoki 'quit' deb yozing>>>"

while True:
    b = input(a)
    if b == "exit" or b == "quit":
        break
    elif float(b)<0:
        continue
    else:
        ildiz = float(b)**(0.5)
        print(f'{b} ning ildizi = {ildiz}')




