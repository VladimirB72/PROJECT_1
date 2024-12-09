
text = '''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.'''


# Extrahujeme slova pomocí regulárního výrazu
slova = text.split() 

# Celkový počet slov
celkem_slov = len(slova)  

# Počet slov začínajících velkým písmenem
slova_zacinajici_velkym = sum(1 for slovo in slova if slovo[0].isupper()) 


# Počet slov psaných velkými písmeny
slova_velkymi_pismeny = sum(1 for slovo in slova if slovo.isupper() and slovo[0].isnumeric()) 
slova_malymi_pismeny = sum(1 for slovo in slova if slovo.islower()) 
 # Počet slov psaných malými písmeny
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
print["cislice"]
# Příklad použití:
#vysledek = analyzuj_text_statistiky(text) :

#print(vysledek)  # Pro zobrazení výstupu spusťte kód.""