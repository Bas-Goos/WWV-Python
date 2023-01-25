def omwisselen():
    getal = int(input("Geef een getal:"))

    laatsteGetal = getal%10
    voorLaatsteGetal = (getal%100)//10
    omgewisseldLaatsteTwee = voorLaatsteGetal + (laatsteGetal*10)

    omgewisseld = (getal-(getal%100)) + omgewisseldLaatsteTwee
    print(omgewisseld)

omwisselen()