print("Python mini viktorīna")

punkti = 0

atbilde = input("1. Kāds atslēgvārds sāk nosacījumu? ").lower()
# TODO: pārbaudi pirmo atbildi un palielini punktu skaitu
if (atbilde == "if"):
    punkti += 1

atbilde = input("2. Kāda funkcija izvada tekstu? ").lower()
# TODO: pārbaudi otro atbildi un palielini punktu skaitu
if (atbilde == "print"):
    punkti += 1

atbilde = input("3. Kāds cikls iet cauri elementiem? ").lower()
# TODO: pārbaudi trešo atbildi un palielini punktu skaitu
if (atbilde == "for"):
    punkti += 1

print(f"Tu ieguvi {punkti} no 3 punktiem.")


