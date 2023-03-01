def loperZet():
    kolom1 = int(input("Geef het getal van kolom 1: "))
    rij1 = int(input("Geef het getal van rij 1:    "))
    kolom2 = int(input("Geef het getal van kolom 2: "))
    rij2 = int(input("Geef het getal van rij 2:    "))

    if abs(rij1 - rij2) == abs(kolom1 - kolom2):
        print('GELDIGE LOPERZET')
    else:
        print('ONGELDIGE LOPERZET')

loperZet()