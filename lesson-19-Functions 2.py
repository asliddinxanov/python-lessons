# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 07:47:19 2022

@author: asliddinxanov
"""

#Functions02

def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"{ism.title()} ning bahosini kiriting: ")
        baholar[ism] = int(baho)
    return baholar

talaba = ['ali', 'vali', 'hasan', 'husan']
a = bahola(talaba[:])
print(a)

print(talaba)

# =============================================================================
# 
# =============================================================================

def katta_haft(matnlar):
    for i in range(len(matnlar)):
        matnlar[i] = matnlar[i].title()
    return matnlar

s = ['ali', 'vali', 'hasan', 'husan']
b = katta_haft(s[:])
print(b)
print(s)

# =============================================================================
# 
# =============================================================================

def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = int(input(f"{ism.title()}ning baholis? >>> "))
        baholar[ism] = baho
    return baholar

talaba = ['ali', 'vali', 'hasan', 'husan']
a = bahola(talaba[:])
print(a)
print(talaba)

# =============================================================================
# *args 
# =============================================================================

def summa(*son):
    return sum(son)

print(summa(1,2,3,4,5))

# =============================================================================
# 
# =============================================================================

def summa(*son):
    a = 0
    for n in son:
        a += n
    return a

print(summa(1,2,3,4,5,6,7))

# =============================================================================
# 
# =============================================================================

def summa(*son):
    a = 1
    for n in son:
        a *= n
    return a

print(summa(1,2,3,4,5,6,7))

# =============================================================================
# **kwargs
# =============================================================================

def avto_info(comp, model, **malumotlar):
    malumotlar['kompanya'] = comp
    malumotlar['modeli'] = model
    return malumotlar

avto1 = avto_info('GM', 'Nexia', yili=2009, rangi = 'oq')
print(avto1)