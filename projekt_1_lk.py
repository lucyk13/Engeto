'''
author = Lucie Kunová
'''
TEXTS = ['''Situated about 10 miles west of Kemmerer, Fossil Butte is a ruggedly impressive topographic feature that rises sharply some 1000 feet above Twin Creek Valley to an elevation of more than 7500 feet above sea level. The butte is located just north of US 30N and the Union Pacific Railroad, which traverse the valley.''',

'''At the base of Fossil Butte are the bright red, purple, yellow and gray beds of the Wasatch Formation. Eroded portions of these horizontal beds slope gradually upward from the valley floor and steepen abruptly. Overlying them and extending to the top of the butte are the much steeper buff-to-white beds of the Green River Formation, which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects a portion of the largest deposit of freshwater fish fossils in the world. The richest fossil fish deposits are found in multiple limestone layers, which lie some 100 feet below the top of the butte. The fossils represent several varieties of perch, as well as other freshwater genera and herring similar to those in modern oceans. Other fish such as paddlefish, garpike and stingray are also present.'''
]

USERS = ("bob", "ann", "mike", "liz")
PASSWORDS = ("123", "pass123", "password123", "pass123")
ODDELOVAC = ("=" * 30)

# 1. Vyžádá si od uživatele přihlašovací jméno a heslo. 
uzivatelske_jmeno = input("Zadej své uživatelské jméno: ")
heslo = input("Zadej své heslo: ")
print(f"Username je: {uzivatelske_jmeno}")
print(f"Heslo je: {heslo}")
print(ODDELOVAC)

# 2. Zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů. 
# 3. Pokud je uživatel registrovaný, pozdrav jej a umožni mu analyzovat texty. Pokud není, upozorni jej a ukonči program. 

if uzivatelske_jmeno in USERS and heslo in PASSWORDS:
  print("Vítej v analýze textů.")
else:
  print("Špatné jméno nebo heslo.")
  exit()
print(ODDELOVAC)

# 4. Program nechá uživatel vybrat mezi třemi texty, uloženými v proměnné TEXTS. Pokud uživatel vybere takové číslo textu, které není v zadání, program jej upozorní a skončí. Pokud uživatel zadá jiný vstup než číslo, program jej rovněž upozorní a skončí. 

cislo_textu = int(input("Zadej číslo textu, který chceš zanalyzovat. Vyber číslo 1 - 3: "))
print(ODDELOVAC)

if cislo_textu == 1:
  vybrany_text = TEXTS[0]
  print("Analyzovaný text má číslo: ", cislo_textu, "a zní: ", vybrany_text)
elif cislo_textu == 2:
  vybrany_text = TEXTS[1]
  print("Analyzovaný text má číslo: ", cislo_textu, "a zní: ", vybrany_text)
elif cislo_textu == 3:
  vybrany_text = TEXTS[2]
  print("Analyzovaný text má číslo: ", cislo_textu, "a zní: ", vybrany_text)
else:
  print("Toto číslo textu nemáme v databázi.")
  exit()

print(ODDELOVAC)
print("Statistika textu je: ")

#5. Pro vybraný text spočítá následující statistiky:
#- počet slov
text_rozdelen_na_slova = vybrany_text.split(" ")

rozdeleny_text = []
for slovo in text_rozdelen_na_slova:
  ciste = slovo.strip(".,")
  rozdeleny_text.append(ciste)
#print(rozdeleny_text)

pocet_slov = len(rozdeleny_text)
print(f"Počet slov v textu je: {pocet_slov}")

#- počet slov začínajících velkým písmenem,
velka_pismena = sum(1 for elem in rozdeleny_text if elem.istitle())
print(f"Počet slov začínající na velké písmeno je: {velka_pismena}")

#- počet slov psaných velkými písmeny,
vse_velka_pismena = sum(1 for elem in rozdeleny_text if elem.isupper())
print(f"Počet slov psaných velkými písmeny je: {vse_velka_pismena}")

#- počet slov psaných malými písmeny,
mala_pismena = sum(1 for elem in rozdeleny_text if elem.islower())
print(f"Počet slov psaných malými písmeny je: {mala_pismena}")

#- počet čísel (ne cifer),
pocet_cislic = sum(1 for elem in rozdeleny_text if elem.isnumeric())
print(f"Počet číslic je: {pocet_cislic}")

txt = rozdeleny_text
cisla = {int(s) for s in txt if s.isdigit()}
#print(cisla)

suma_cisel = sum(cisla)

print(f"Suma čísel je: {suma_cisel}")

print(ODDELOVAC)

#6. Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu.

print("délka|  počet  |výskyt")
print(ODDELOVAC)

delky = []
for slovo in rozdeleny_text:
  delka = len(slovo)
  delky.append(delka)

#print(delky)

slovnik_vyskytu = {}
for delka in delky:
  slovnik_vyskytu[delka] = slovnik_vyskytu.get(delka, 0) + 1
#print(slovnik_vyskytu)

cetnosti = sorted(slovnik_vyskytu)

for index, _ in enumerate(slovnik_vyskytu):
  print(f"_" * 30)
  for item in cetnosti:
    pocet_pismen = int(slovnik_vyskytu[item])
    print((item), (pocet_pismen) * "*" , (pocet_pismen))
    cetnosti.remove(item)
    break

print(ODDELOVAC)
