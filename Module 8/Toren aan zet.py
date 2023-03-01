def torenzet():
    kolom1 = int(input("Geef het getal van kolom 1: "))
    rij1 = int(input("Geef het getal van rij 1:    "))
    kolom2 = int(input("Geef het getal van kolom 2: "))
    rij2 = int(input("Geef het getal van rij 2:    "))

    if rij1 == rij2 or kolom1 == kolom2:
        print('GELDIGE TORENZET')
    else:
        print('ONGELDIGE TORENZET')

torenzet()