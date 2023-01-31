def somCijfers():
    getal = int(input("Geef een getal:  "))

    hondertal = getal//100
    tiental = (getal - (hondertal*100))//10
    eenheden = getal%10

    som = hondertal + tiental + eenheden

    print(som)

somCijfers()