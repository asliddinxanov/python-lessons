# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 10:39:41 2022

@author: asliddinxanov
"""

# CLASS

# class user:
#     def __init__(self,nic,fism,emile,tyil):
#         self.nic = nic
#         self.fism = fism
#         self.emile = emile
#         self.tyil = tyil

#     def get_info(self):
#         print(f"Salom, ismim {self.fism.title()}, {self.tyil} yilda tug'ilganman "
#               f"emile: {self.emile}")

# user1 = user("vali2002","vali","2002@mail.ru",2002)
# user1.get_info()

# # =============================================================================
# # 
# # =============================================================================

# class user:
#     def __init__(self,nic,fism,emile,tyil):
#         self.nic = nic
#         self.fism = fism
#         self.emile = emile
#         self.tyil = tyil
        
#     def get_id(self):
#         return self.nic
    
#     def get_username(self):
#         return self.fism
    
#     def get_emile(self):
#         return self.emile
    
#     def get_age(self,yil):
#         return yil - self.tyil
    
# user1 = user("vali2002","vali","2002@mail.ru",2002)

# # =============================================================================
# # class va class ichida qo'shimcha kiritish usullari
# # =============================================================================

# class Student:
#     def __init__(self,ism,fam,tyil):
#         self.ism = ism
#         self.fam = fam
#         self.tyil = tyil
#         self.course = 1
        
#     def get_info(self):
#         return f"{self.fam} {self.ism}. {self.tyil}-yilda tug'ilgan. {self.course} kurs talabasi"
    
#     def get_name(self):
#         return self.ism
    
#     def get_lastname(self):
#         return self.fam
    
#     def set_cousre(self,new_course):
#         self.cousre = new_course
        
#     def update_course(self):
#         self.course += 1
    
# class Fan():
#     """Fan nomli class"""
#     def __init__(self,nomi):
#         self.nomi = nomi
#         self.students_son = 0
#         self.students = []
    
#     def add_student(self,student):
#         """Fan-ga talabalar qo'shish"""
#         self.students.append(student)
#         self.students_son += 1
    
#     def get_name(self):
#         """Fan nomi"""
#         return self.nomi
    
#     def get_students(self):
#         """Fanga yozilgan talabalar hoqida ma'lumot!"""
#         return [x.get_info() for x in self.students]
#     """bu yerda students dagi xar bir ma'lumotni olib 
#         x ga joylab uni get_info ga berayapti"""
# """ 
#     students = []
#     for x in self.students:
#     students.append(x.get_info())
#     retunen students
    
#     ni o'rniga ishlatdik"""
    
# def see_methods(klass):
#     return [method for method in dir(klass) if method.startswith('__') is False]
#     """bu klasss yordamida dir() orqali chiqadigan methodlar ro'yxatidagi 
#         __ bilan boshlanadigan ro'yxayni o'chirib biz yozgan methodlarnigina
#         ko'rdatadigan method buni ishlatish uchun >> see_methods(Student) <<<
#         ni ni konsolda yozish bilan chiqaruladi. Bu yerda Student class nomi"""
       
# matem = Fan("Oliy Matematika")    
# student1 = Student("Ali", "Valiev", 1995)
# student2 = Student("Akmal", "Aliev", 2000)
# student3 = Student("Nigina", "Solieva", 2003)

# matem.add_student(student1)
# matem.add_student(student2)
# matem.add_student(student3)

# print(matem.students_son)
# print(matem.students)
# mat_students = matem.get_students()
# print(mat_students)

# print(see_methods(Student)) # classda ishlatilgan methodlani chiqaradi
# print(see_methods(student1))

# # print(see_methods(str))
# print(student1.__dict__) # o'zgaruvchiga berilgan so'zlarni chiqaradi
# print(student1.__dict__.keys()) # kalit so'z (key) larni chiqaradi

# # =============================================================================

# # =============================================================================

class Avto:
    def __init__(self,model,color,kp):
        self.model = model
        self.color = color
        self.kp = kp
        self.km = 0
        
    def get_info(self):
        return f"model: {self.model}, rangi: {self.color}, karobka: {self.kp}. {self.km}km bosib o'tgan"
    
    def set_km(self,new_km):
        self.km = new_km
        
    def update_km(self):
        self.km += 1000
        
class Salon():
    def __init__(self,nomi):
        self.nomi = nomi
        self.avto_son = 0
        self.avtos = []
        
    def get_name(self):
        return self.nomi
    
    def add_avto(self,avto):
        self.avtos.append(avto)
        self.avto_son += 1
        
    def get_avtos(self):
        return [x.get_info() for x in self.avtos]
    
salon = Salon("GM")        
avto1 = Avto("Lacetti", "white", "avto")
avto2 = Avto("Nexia", "black", "manual") 
avto3 = Avto("Malibu", "black", "avto") 

salon.add_avto(avto1)
salon.add_avto(avto2)
salon.add_avto(avto3)

# print(salon.get_avtos())

def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]

# print(see_methods(Salon))
# print(see_methods(Avto))
print(avto1.update_km()) #bu avto1 dagi ma'lumotni kmni o'zgartiradi
print(salon.get_avtos())