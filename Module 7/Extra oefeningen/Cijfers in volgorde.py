def CijfersVolgorde():
    getal = int(input("Geef een natuurlijk getal tussen honderd en duizend: "))

    hondertal = getal // 100
    getal -= hondertal*100
    tiental  = getal // 10
    eenheid = getal % 10

    if hondertal < tiental < eenheid:
        print("STIJGEND")
    else:
        print("NIET (!) STIJGEND")

CijfersVolgorde()