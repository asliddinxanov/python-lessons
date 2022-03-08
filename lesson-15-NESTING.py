# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 09:30:18 2022

@author: asliddinxanov
"""

# Nesting 

car0 = {
        "model": "bmw",
        "color": "red",
        "year": "2020",
        "price": "45000"}
car1 = {
        "model": "audi",
        "color": "yellow",
        "year": "2021",
        "price": "85000"}
car2 = {
        "model": "tesla",
        "color": "white",
        "year": "2021",
        "price": "79000"}

cars = [car0, car1, car2]
for car in cars:
    print(f"{car['model'].title()}, "
          f"{car['color']}, "
          f"{car['year']}y ",
          f"{car['price']}$")
# =============================================================================

# =============================================================================
bmws = []
for n in range(10):
    new_car = {
        "model": "bmw",
        "color": None,
        "year": 2020,
        "km" : 0,
        "cpc" : "avto",
        "price" : None}
    
    bmws.append(new_car)
    for bmw in bmws[:3]:
        bmw["color"] = "red"
        bmw["km"] = 15000
    
    for bmw in bmws[3:6]:
        bmw["color"] = "blue"
        bmw["cpc"] = "manual"
        bmw["km"] = 25000
        
    for bmw in bmws[6:]:
        bmw["color"] = "white"
        bmw["km"] = 10000
    
    for bmw in bmws:
        if bmw["cpc"] == "avto":
            bmw["price"] = 74000
        else:
            bmw['price'] = 69000
for bmw in bmws:
    print(f"{bmw['model']}, "
          f"{bmw['color']}, "
          f"{bmw['year']}y, "
          f"km:{bmw['km']}, "
          f"cpc:{bmw['cpc']}, "
          f"{bmw['price']}$.")
print("\n")
# =============================================================================
# dictionary in list
# =============================================================================
buxoriy = {'ism' : 'Abu Abdulloh Muhammad inb Ismoil',
            'tyili' : 810,
            'vyili': 870,
            'tjoyi' : 'Buxoro'
            }
qodiriy = {'ism' : 'Abdullo Qodiriy',
            'tyili' : 1894,
            'vyili': 1938,
            'tjoyi' : 'Toshkent'
            }
vohidov = {'ism' : 'Erkin Vohidov',
            'tyili' : 1936,
            'vyili': 2016,
            'tjoyi' : 'Farg\'ona'
            }
navoiy = {'ism' : 'Alisher Navoiy',
            'tyili' : 1441,
            'vyili': 1501,
            'tjoyi' : 'Xirot'
            }
persons = [buxoriy, qodiriy, vohidov, navoiy]

for a in persons:
    ism = a['ism']
    tyil = a['tyili']
    vyil = a['vyili']
    tjoy = a['tjoyi']
    print(f"{ism} {tyil}yilda {tjoy}da tug'ilib " 
          f"{tyil-vyil}yil umir ko'rgan.")
# =============================================================================

# =============================================================================
buxoriy = {'ism' : 'Abu Abdulloh Muhammad inb Ismoil',
            'tyili' : 810,
            'vyili': 870,
            'tjoyi' : 'Buxoro',
            'asari' : ["Al-jome’ as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sag'ir"]
            }
qodiriy = {'ism' : 'Abdullo Qodiriy',
            'tyili' : 1894,
            'vyili': 1938,
            'tjoyi' : 'Toshkent',
            'asari' : ["O'tkan kunlar","Mehrobdan Chayon",'Obid ketmon']
            }
vohidov = {'ism' : 'Erkin Vohidov',
            'tyili' : 1936,
            'vyili': 2016,
            'tjoyi' : 'Farg\'ona',
            'asari' : ["Tong nafasi","Qo'shiqlarim sizga","O'zbegim","Qiziquvchan Matmusa"]
            }
navoiy = {'ism' : 'Alisher Navoiy',
            'tyili' : 1441,
            'vyili': 1501,
            'tjoyi' : 'Xirot',
            'asari' : ["Xamsa","Lison ut-Tayr","Mahbub Al-Qulub",'Munojot']
            }
shaxslar = [buxoriy, qodiriy, vohidov, navoiy]

for n in shaxslar:
    ism = n['ism']
    asar = n['asari']
    print(f"{ism}ning asarlari: ")
    for m in asar:
        print(m)
    print("\n")
# =============================================================================
# dictionary in dictionary
# =============================================================================
davlatlar = {
    "o'zbekiston":{'poytaxt':"toshkent",
                    'maydon':448978,
                    'aholi':33_000_000,
                    'pul birligi':"so'm"
                    },
    "rossiya":{'poytaxt':"moskva",
                    'maydon':17_098_246,
                    'aholi':144_000_000,
                    'pul birligi':"rubl"
                    },
    "aqsh":{'poytaxt':"vashington",
                    'maydon':9_631_418,
                    'aholi':327_000_000,
                    'pul birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                    'maydon':329750,
                    'aholi':25_000_000,
                    'pul birligi':"rinngit"}
    }

for d, info in davlatlar.items():
    if d.lower()=='aqsh':
        d = d.upper()
    else:
        d = d.capitalize()
    print(f"\n{d}ning poytaxti {info['poytaxt'].title()}"
          f"\nHududi: {info['maydon']} kv.km"
          f"\nAholisi: {info['aholi']}"
          f"\nPul birligi: {info['pul birligi']}")
# =============================================================================

# =============================================================================
davlatlar = {
    "o'zbekiston":{'poytaxt':"toshkent",
                    'maydon':448978,
                    'aholi':33_000_000,
                    'pul birligi':"so'm"
                    },
    "rossiya":{'poytaxt':"moskva",
                    'maydon':17_098_246,
                    'aholi':144_000_000,
                    'pul birligi':"rubl"
                    },
    "aqsh":{'poytaxt':"vashington",
                    'maydon':9_631_418,
                    'aholi':327_000_000,
                    'pul birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                    'maydon':329750,
                    'aholi':25_000_000,
                    'pul birligi':"rinngit"}
    }

d = input('Davlat nomini kiriting: ').lower()
if d in davlatlar:
    info = davlatlar[d]
    print(f"\n{d.capitalize()}ning poytaxti {info['poytaxt'].title()}"
          f"\nHududi: {info['maydon']} kv.km"
          f"\nAholisi: {info['aholi']}"
          f"\nPul birligi: {info['pul birligi']}")
else:
    print("Sorry not found!!!")