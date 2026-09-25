print("Biļešu cenas kalkulators")

vecums = int(input("Ievadi savu vecumu: "))

cena = 0

if vecums <= 6:
    cena = 0
elif 7 <= vecums <= 17:
    cena = 3
elif 18 <= vecums <= 64:
    cena = 7
else:
    cena = 4


print(f"Biļetes cena ir {cena} EUR.")


