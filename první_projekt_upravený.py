"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Vladimír Bořek
email: borek.vladimir@iex.cz
"""


TEXTS = [
    """
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. """,
    """At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.""",
    """The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present."""
]

oddelovaci_radek = "-" * 40


# slovník uživatelů

users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

# ověření uživatele

username = input("username:")
password = input("password:")


if users.get(username) != password:
    print("unregristered user, terminanting the program .")
    exit()
else:
    print(oddelovaci_radek)
    print("Wecome to the app ,", username)
    print("We have 3 texts to be analyzed.")
    print(oddelovaci_radek)
    vyber = input("Enter a number btw. 1 and 3 to select: ")
    print(oddelovaci_radek)

if not vyber.isnumeric():

    print("You not insert number, terminanting the program")
    exit()
else:

    volba = int(vyber)

if not 1 <= volba <= 3:

    print("Your number is not btw. 1 and 3 .")
    exit()
else:

    slova = TEXTS[volba - 1].split()

celkem_slov = 0
slova_zacinajici_velkym = 0
slova_velkymi_pismeny = 0
slova_malymi_pismeny = 0
cisla = 0
soucet = 0
delky_slov = {}

# Procházení textu

for slovo in slova:
    celkem_slov += 1
    delka = len(slovo.strip(",.:;").lower())
    delky_slov[delka] = delky_slov.setdefault(delka, 0) + 1
    if slovo[0].isupper():
        slova_zacinajici_velkym += 1
    if slovo.isupper() and not slovo[0].isnumeric():
        slova_velkymi_pismeny += 1
    if slovo.islower():
        slova_malymi_pismeny += 1
    if slovo.isdigit():
        cisla += 1
        soucet += int(slovo)

# Tisk výstupů

print(f"There are {celkem_slov} words in the selected text.")
print(f"There are {slova_zacinajici_velkym} titlecase words.")
print(f"There are {slova_velkymi_pismeny} uppercase words.")
print(f"There are {slova_malymi_pismeny} lowercase words.")
print(f"There are {cisla} numeric strings.")
print(f"The sum of all the numbers is {soucet}.")

# Vytvoření seznamu dvojic (délka, počet)

seznam_delek = list(delky_slov.items())

seznam_delek.sort()

# Tisk tabulky

print(oddelovaci_radek)
print("LEN|    OCCURENCES      | NR.")
print(oddelovaci_radek)

for delka, pocet in seznam_delek:

    print(f"{delka:>3} |{"*" * pocet :<20}| {pocet :<3}")

    print(oddelovaci_radek)
