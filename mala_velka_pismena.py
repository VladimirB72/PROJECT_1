
text = '''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The Fossils
represent several varieties OF perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''


slova = text.split()  # Extrahujeme slova pomocí regulárního výrazu
celkem_slov = len(slova)  # Celkový počet slov
slova_zacinajici_velkym = sum(1 for slovo in slova if slovo[0].isupper())  # Počet slov začínajících velkým písmenem
slova_velkymi_pismeny = sum(1 for slovo in slova if slovo.isupper())  # Počet slov psaných velkými písmeny
slova_malymi_pismeny = sum(1 for slovo in slova if slovo.islower())  # Počet slov psaných malými písmeny
cislice = sum(1 for slovo in slova if slovo.isnumeric())
statistiky = {
        "celkem_slov": celkem_slov,
        "slova_zacinajici_velkym": slova_zacinajici_velkym,
        "slova_velkymi_pismeny": slova_velkymi_pismeny,
        "slova_malymi_pismeny": slova_malymi_pismeny,
        "cislice":cislice
    }
#return statistiky  # Vracíme slovník se statistikami
print("Ve vybraném textu je :", celkem_slov,"slov.")
print("Ve vybraném textu je :", slova_zacinajici_velkym, "slov začínající velkým písmenem.")
print("Ve vybraném textu je :", slova_velkymi_pismeny, "slov velkými písmeny.")
print("Ve vybraném textu je :", slova_malymi_pismeny, "slov malými písmeny.")
print(statistiky)
print(cislice)
# Příklad použití:
#vysledek = analyzuj_text_statistiky(text) :

#print(vysledek)  # Pro zobrazení výstupu spusťte kód.""