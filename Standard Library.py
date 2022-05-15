# -*- coding: utf-8 -*-
"""
Created on Sun May 15 08:10:16 2022

@author: asliddinxanov
"""
# Standard Librarys

# # datatime
import datetime as dt

# now = dt.datetime.now()
# print(time_now) #xozirgi sanani qaytaradi

# print(now.date()) #faqat sanani chiqaradi

# print(now.hour) #soat
# print(now.minute) #min
# print(now.second) #secund

# # data()

# today = dt.date.today()
# print(f"Bugun {today}chi sana")
# # sanani qo'lda kiritish uchun
# tomorrow = dt.date(2022, 5, 16)
# print(f"etaga {tomorrow}chi sana")

# # time()

# t =  dt.datetime.now() # sozirgi vaqtni
# t_now = t.time()
# print(t_now)
# t_keyin = dt.time(9, 33, 43)
# print(t_keyin)

# # kunni ayirish

# now = dt.date.today()
# bd = dt.date(2022,3,4)
# bd_f = bd - now
# # kunni o'zini olish uchun .days()
# print(f"Tug'ilgan kunga {bd_f.days}-kun qoldi")

now = dt.datetime.now()
match_t = dt.datetime(2022, 5, 20, 12, 45, 00)
match = match_t - now
# print(match)
minut = int(match.seconds/60)
hour = int(minut/60)
print(f"O'yin boshlanishiga {match.days} kunu {hour}-soat qoldi")