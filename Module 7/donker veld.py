def donkerVeld():
    kolom = int(input("Geef het kolomnummer:    "))
    rij = int(input("Geef het rijnummer:    "))

    if kolom % 2 == 0:
        kolomEven = True
    else:
        kolomEven = False

    if rij % 2 == 0:
        rijEven = True
    else:
        rijEven = False
    
    if kolomEven == rijEven:
        print('DONKER VELD')
    else:
        print('LICHT VELD')

donkerVeld()