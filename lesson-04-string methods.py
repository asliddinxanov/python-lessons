# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 11:51:39 2022

@author: asliddinxanov
"""
#upper() and lower()

name = "James"
surname = "Bond"
name1 = "james"
surname1 = "bond"
print(f"{name1.upper()} {surname1.upper()}") #xamasini katta xarfga o'giradi
print(f"{name.lower()} {surname.lower()}") #xamasini kichkina xarfga o'giradi
name_surname = f"{name} {surname}"
print(name_surname.upper())
print(name_surname.lower())

#title() and capitalize()

word = "yozilgan xar bitta so'zni bosh xarfni katta xarfga o'girish."
print(word.title())
word_2 = "yozilgan gapni bosh xarfini katta xarfga o'girish."
print(word_2.capitalize())

name_surname = "james bond"
print(name_surname.capitalize())

#strip(), rstrip() and lstrip() methods

a = "   is   "
print("Time"+ a +" money")
print("Time"+ a.strip()+" money")
print("Time"+ a.rstrip()+" money")
print("Time"+ a.lstrip()+" money")

#input 

name = input("What's your name? >>>")
surname = input("What's your surname? >>>")
name_surname = f"{name.title()} {surname.title()}"
print(f"Hello {name_surname}")

#M

name = input("Ismingiz nima? >>>")
surname = input("Familiyangiz nima? >>>")
maqsad = input("Nega bu o'qishni tanladingiz? >>>")
shiyor = input("Hayotdan shioringiz. >>>")

print(f"Salom men {name.upper()} {surname.upper()} bo'laman.\n"
      f"Maqsadingiz? : {maqsad.capitalize() }"
      f"Hayotdan shioringiz : {shiyor.title()}")




