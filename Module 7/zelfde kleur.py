def kleurVeld(kolom, rij):

    if kolom % 2 == 0:
        kolomEven = True
    else:
        kolomEven = False

    if rij % 2 == 0:
        rijEven = True
    else:
        rijEven = False
    
    if kolomEven == rijEven:
        return('DONKER VELD')
    else:
        return('LICHT VELD')

kolom1 = int(input("Geef het kolomnummer van veld 1:    "))
rij1 = int(input("Geef het rijnummer van veld 1:    "))
kolom2 = int(input("Geef het kolomnummer van veld 2:    "))
rij2 = int(input("Geef het rijnummer van veld 2:    "))

kleurVeld1 = kleurVeld(kolom1, rij1)
kleurVeld2 = kleurVeld(kolom2, rij2)

if kleurVeld1 == kleurVeld2:
    print('DEZELFDE KLEUR')
else:
    print('VERSCHILLENDE KLEUR')