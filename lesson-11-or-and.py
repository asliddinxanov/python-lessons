# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 08:01:00 2022

@author: asliddinxanov
"""

# OR AND

kun = input("Bugun qaysi kun >>>")
if kun.lower() == "shanba" or kun.lower() == "yakshanba":
    p = "Bugun dam olish kuni"
else:
    p = "Bugun ish kuni"
print(p)

#----------

kun = input("Bugun qaysi kun >>>")
d = float(input("bungungi haroratni kiriting >>>"))
if kun.lower() == "shanba" or kun.lower() == "yakshanba" and d >= 25:
    p = "Bugun cho'milishga borsa bo'ladi"
elif kun.lower() == "shanba" or kun.lower() == "yakshanba" and d <= 25:
    p = "Bugun cho'milish tafsiya qilinmaydi"
else:
    p = "Bugun ish kuni"
print(p)