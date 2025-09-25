emri = input("Emri: ").strip()
mosha = int(input("Mosha: "))
cmimi_baze = float(input("Cmimi baze (Lek): "))
kupon = input("Ke kupon? (po/jo): ").lower().strip()

if len(emri) < 2 or mosha < 10 or mosha > 99 or cmimi_baze <= 0:
    print("Te dhenat jane te pavlefshme!")
else:
    zbritje_moshe = 0.10 if mosha < 18 or mosha >= 65 else 0
    zbritje_kupon = 0.05 if kupon in ["po", "yes", "y"] else 0
    zbritje_rinore = 0.03 if mosha <= 23 and cmimi_baze >= 1000 else 0

    zbritje_totale = zbritje_moshe + zbritje_kupon + zbritje_rinore
    vlere_zbritje = cmimi_baze * zbritje_totale
    pas_zbritjes = cmimi_baze - vlere_zbritje
    tvsh = pas_zbritjes * 0.15
    total = pas_zbritjes + tvsh

    print("------------------------------")
    print("Klient:", emri, "(mosha", mosha, ")")
    print("Cmimi baze:", format(cmimi_baze, '.2f'), "Lek")
    print("Zbritje totale:", str(round(zbritje_totale * 100, 2)) + "%", "(vlere:", format(vlere_zbritje, '.2f'), "Lek)")
    print("Pas zbritjes:", format(pas_zbritjes, '.2f'), "Lek")
    print("TVSH (15%):", format(tvsh, '.2f'), "Lek")
    print("Totali:", format(total, '.2f'), "Lek")
