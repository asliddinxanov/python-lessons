# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 08:44:20 2022

@author: asliddinxanov
"""
# Inheritance - Vorislik

class Shaxs:
    def __init__(self,ism,fam,passport,tyil):
        """shaxs xususiyatlari"""
        self.ism = ism
        self.fam = fam
        self.passport = passport
        self.tyil = tyil
        
    def get_info(self):
        """shaxs malumot"""
        info = f"{self.ism} {self.fam}. "
        info += f"{self.tyil}-yilda tug'ilgan. Passport No:{self.passport}"
        return info
    
    def get_age(self,yil):
        """shaxs yoshi"""
        return yil - self.tyil
    
class Student(Shaxs):
    def __init__(self,ism,fam,passport,tyil,idnum,addres):
        """tepadagi shaxs classidan xususiyat olish"""
        super().__init__(ism,fam,passport,tyil) #bu yerda (:)belgisi yo'q
        self.idnum = idnum
        self.course = 1
        self.addres = addres
        
    def get_id(self):
        return self.idnum
    
    def get_course(self):
        return self.course
    
    def update_course(self):
        self.course += 1
        
    def get_info(self): #POLIMORFIZM
        info = f"{self.ism} {self.fam}. "
        info += f"{self.tyil}-yilda tug'ilgan. Passport No:{self.passport} "
        info += f"Talabalik ID No:{self.idnum}. "
        return info
    
class Addres:
    def __init__(self,uy,kocha,tum,vil):
        self.uy = uy
        self.kocha = kocha
        self.tum = tum
        self.vil = vil
        
    def get_addres(self):
        addres = f"{self.vil}-viloyati, {self.tum}-tumani, "
        addres += f"{self.kocha}  No:{self.uy}chi uy"
        return addres
    
shaxs = Shaxs("Ali", "Valiev", "ZZ777777", 2002)
student_addres = Addres(19, "Navro'z", "Olmazor", "Samarqand")
student = Student("Ali", "Valiev", "ZZ777777", 2002, "S20000", student_addres)

# print(shaxs.get_age(2022))
print(student.get_info())
print(student.addres.get_addres())