def getallenRij():
    getal1 = int(input("Geef het onderste getal van de rij: "))
    getal2 = int(input("Geef het bovenste getal van de rij: "))

    rij = str(getal1)

    if getal1 < getal2:
        while getal1 < getal2:
            getal1 += 1
            rij += " " + str(getal1)

    if getal2 < getal1:
        while getal1 > getal2:
            getal1 -= 1
            rij += " " + str(getal1)

    print(rij)

getallenRij() 