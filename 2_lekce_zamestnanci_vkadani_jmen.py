# vytvořím list zamestnaci
zamestnanci = [
    "František", "Anna",
    "Jakub", "Klára"
] 

# vpis zamestnanci na začátku
print("Zaměstnanci na začátku:", zamestnanci)

# vytvoření kopie listu zamestnanci
zamestnanci_a = zamestnanci.copy()
zamestnanci_a.append("Bruno")
zamestnanci_a.append("Anežka")

# výpis zaměstnanci + nová jména
print("Nová jména přidána :" , zamestnanci_a)

# vytvoření kopie zamestnanci , proměnná zamestnanci_b
zamestnanci_b = zamestnanci.copy()
zamestnanci_b.insert(1, "Bruno")

#print(zamestnanci_b , aktualni list)
print("Nová jména vložena :" , zamestnanci_b)