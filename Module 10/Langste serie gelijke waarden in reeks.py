def langsteSerie():
    gelijkeWaarden = 0
    gelijkeWaardenMax = 0
    vorigeInvoer = 0 

    while True:
        invoer = int(input("Geef een getal: "))
        if invoer == 0:
            break
        if invoer == vorigeInvoer:
            gelijkeWaarden += 1
        else:
            gelijkeWaarden = 0
            vorigeInvoer = invoer
        if gelijkeWaarden > gelijkeWaardenMax:
            gelijkeWaardenMax = gelijkeWaarden

    print(gelijkeWaardenMax+1)

langsteSerie()