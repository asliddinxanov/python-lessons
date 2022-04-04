# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 10:39:41 2022

@author: asliddinxanov
"""

# CLASS

class user:
    def __init__(self,nic,fism,emile,tyil):
        self.nic = nic
        self.fism = fism
        self.emile = emile
        self.tyil = tyil

    def get_info(self):
        print(f"Salom, ismim {self.fism.title()}, {self.tyil} yilda tug'ilganman "
              f"emile: {self.emile}")

user1 = user("vali2002","vali","2002@mail.ru",2002)
user1.get_info()

# =============================================================================
# 
# =============================================================================

class user:
    def __init__(self,nic,fism,emile,tyil):
        self.nic = nic
        self.fism = fism
        self.emile = emile
        self.tyil = tyil
        
    def get_id(self):
        return self.nic
    
    def get_username(self):
        return self.fism
    
    def get_emile(self):
        return self.emile
    
    def get_age(self,yil):
        return yil - self.tyil
    
user1 = user("vali2002","vali","2002@mail.ru",2002)
