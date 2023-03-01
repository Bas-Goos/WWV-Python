def paardenveld():
    kolom1 = int(input("Geef het getal van kolom 1: "))
    rij1 = int(input("Geef het getal van rij 1:    "))
    kolom2 = int(input("Geef het getal van kolom 2: "))
    rij2 = int(input("Geef het getal van rij 2:    "))

    afstand = (((kolom1 - kolom2) ** 2) + ((rij1 - rij2) ** 2))**(1/2)
    if afstand == 5**(1/2):
        print('GELDIGE ZET')
    else:
        print('ONGELDIGE ZET')

paardenveld()