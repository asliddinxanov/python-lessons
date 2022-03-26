# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 10:39:33 2022

@author: asliddinxanov
"""

# =============================================================================
# Find number game
# =============================================================================

import random as r

print("Topqirlik o'yini")
def findnum(x=10):
    pc = r.randint(1,x)
    marta1 = 0
    input(f"1dan {x}gacha son o'yladim, topish uchun istalgan tugmani bosing.")
    
    while True:
        marta1 += 1
        user = int(input("Sonni kiriting>>>"))
        if user < pc:
            print(f"Xato!!! Men o'ylagab sin {user} dan katta!")
        elif user > pc:
            print(f"Xato!!! Men o'ylagan son {user} dan kichik!")
        else:
            break 

    print(f"Topdingiz men o'ylagan ron {pc}edi."
          f"Siz {marta1} urunishda topdingiz.")
    return marta1

def findnum_pc(x=10):
    input("1 dan {x} gach son o'ylab istalgan tugamni bosing.")
    mini = 1
    maxi = x
    marta2 = 0
    
    while True:
        marta2 += 1
        if mini != maxi:
            pc = r.randint(mini,maxi)
        else:
            pc = mini
        user = input(f"Siz o'ylagan son {pc} to'g'rimi? to'g'ti (t)"
                     f"men o'ylagan son bundan katta (+)"
                     f"men o'lagan son bundan kichik (-)".lower())
        if user == "-":
            maxi = pc - 1
        elif user == "+":
            mini = pc + 1
        else:
            break
    print(f"Topdim!!!\n Men {marta2} urunishda toptim")
    return marta2

def play(x=10):
    yana = True
    while yana:
        marta_user = findnum(x)
        marta_pc = findnum_pc(x)
        
        if marta_user < marta_pc:
            print(f"{findnum(x)}Siz yutdingiz.")
        elif marta_user > marta_pc:
            print(f"{findnum_pc(x)}Men yutdim.")
        else:
            print("DURRANG")
        
        yana = int(input("Yana o'ynaymizmi? ha(1), yo'q(0)"))

print(play())