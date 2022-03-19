# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 09:08:28 2022

@author: asliddinxanov
"""

def avto_info(kompaniya, modeli, color, yil=None, price=None):
    avto = {
        'kompaniya': kompaniya,
        'model': modeli,
        'rang': color,
        'yili': yil,
        'narxi': price}
    return avto

# def avto_enter():
#     """avto malumot kiritish"""
#     avtos = []
#     while True:
#         print("Quyidagi malumotlarni kiriting.")
#         kompaniya = input("Iishlab chiqaruvchi: ")
#         modeli = input("Madeli: ")
#         color = input("Rangi: ")
#         yil = int(input("Yili: "))
#         price = int(input("Narxi: "))
#         avtos.append(avto_info(kompaniya, modeli, color, yil, price))
#         j = input("Yana go'shasizmi?(yes/no)")
#         if j == "no":
#             break
#     return avtos

def info_print(avto_info):
    print(f"{avto_info['kompaniya'].title()}, {avto_info['model'].title()}, "
          f"{avto_info['yili']}-yil, rangi {avto_info['rang']},"
          f" narxi-{avto_info['narxi']}$.")