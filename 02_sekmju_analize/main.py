atzimes = [7, 5, 9, 4, 8]

# TODO: aprēķini vidējo, augstāko un zemāko vērtējumu
videja = sum(atzimes)//len(atzimes)
augstaka = max(atzimes)
zemaka = min(atzimes)

# TODO: ar for ciklu saskaiti vērtējumus, kas ir vismaz 4
sekmigo_skaits = 0

for i in range(len(atzimes)):
    if (atzimes[i] >= 4):
        sekmigo_skaits += 1

print(f"Vidējais vērtējums: {videja}")
print(f"Augstākais vērtējums: {augstaka}")
print(f"Zemākais vērtējums: {zemaka}")
print(f"Sekmīgo vērtējumu skaits: {sekmigo_skaits}")


