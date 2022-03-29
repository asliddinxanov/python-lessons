# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 12:00:07 2022

@author: asliddinxanov
"""

import random as r
from uzwords import words
 
print("So'z topish o'yini")

def get_word():
    word = r.choice(words)
    while "-" in word or " " in word:
        word = r.choice(words)
    return word.upper()

def display(user_letters,word):
    display_letter = ""
    for letter in word:
        if letter in user_letters.upper():
            display_letter += letter
        else:
            display_letter += "-"
    return display_letter

def play():
    word = get_word()
    word_letters = set(word)
    user_letters = ""
    print(f"Men {len(word)} xonali so'z o'yladim topaolasizmi???")
    
    while len(word_letters) > 0:
        print(display(user_letters,word))
        if len(user_letters) > 0:
            print(f"Su vaqtdacha kiritgan sonlar {user_letters}")
            
        letter = input("Xarf kiriting>>>").upper()
        if letter in user_letters:
            print("Bu harfni odin kiritgnasiz!!!")
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} xarfi to'g'ri.")
        else:
            print("Bunday xarf yo'q!!!")
        user_letters += letter
    print(f"Tabriklayman {word} so'zini {len(user_letters)} ta urunishda topdingiz!!!")
    
print(play())

