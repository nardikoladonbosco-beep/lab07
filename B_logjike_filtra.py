mosha = int(input("Mosha: "))
karte = input("Ke karte studenti? (po/jo): ").lower().strip()

zbritje_lejuar = mosha < 18 or mosha >= 65 or karte == "po"
print("Zbritje e lejuar:", "PO" if zbritje_lejuar else "JO")

buxheti = float(input("Buxheti (Lek): "))
cmimi = float(input("Cmimi (Lek): "))
blerja_mundur = buxheti >= cmimi
print("Blerja e mundur:", "PO" if blerja_mundur else "JO")

oferta_speciale = (500 <= cmimi <= 2000) and (16 <= mosha <= 25)
print("Oferta speciale:", "PO" if oferta_speciale else "JO")
