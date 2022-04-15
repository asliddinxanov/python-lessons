# -*- coding: utf-8 -*-
"""
Created on Apr 15 11:42:26 2022

@author: asliddinxanov
"""
# *args and **kwargs(keywords arguments)
def summ(*num):
    a = 0
    for son in num:
        a += son
    return a
print(summ(1,2,3,4))
print(summ(2,5,3,5))

# =============================================================================
# 
# =============================================================================

def summ(*num):
    return sum(num)
print(summ(1,2,3,4))
print(summ(2,5,3,5))

# =============================================================================
# 
# =============================================================================

def summ(x,y,z,*num):
    return sum(num)
# print(summ(3,4)) # bu yerda error beradi chunki majburi 3ta son yozish kk edi.
print(summ(2,5,3)) # bu esa 0 chiqaradi chunki "num"ni chiqarishni so'radik.print(summ(1,2,3,4))
print(summ(2,5,3,5)) # 5 

# =============================================================================
# 
# =============================================================================

def avto_info(komp,model,**malumotlar):
    malumotlar['komp'] = komp
    malumotlar['model'] = model
    return malumotlar

avto1 = avto_info("BMW", "M5", color = "Qora", yili = 2022)









