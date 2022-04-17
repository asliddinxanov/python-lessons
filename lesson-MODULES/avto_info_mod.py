# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 09:08:28 2022

@author: asliddinxanov
"""

def avto_info(komp,model,color,kp,year,price=None):
    avto = {'komp' : komp,
            'model' : model,
            'color' : color,
            'kp' : kp,
            'year' : year,
            'price' : price}
    return avto

def avto_enter():
    """avto malumot kiritish"""
    avtos = []
    while True:
        print("Quyidagi malumotlarni kiriting.")
        kompaniya = input("Iishlab chiqaruvchi: ")
        modeli = input("Madeli: ")
        color = input("Rangi: ")
        yil = int(input("Yili: "))
        price = int(input("Narxi: "))
        avtos.append(avto_info(kompaniya, modeli, color, yil, price))
        j = input("Yana go'shasizmi?(yes/no)")
        if j == "no":
            break
    return avtos

def info_print(avto_info):
    print(f"{avto_info['color'].title()}, {avto_info['komp'].upper()}, "
          f"{avto_info['model'].upper()}, {avto_info['kp']} karobka, "
          f"{avto_info['year']} - yil, {avto_info['price']}$.")
