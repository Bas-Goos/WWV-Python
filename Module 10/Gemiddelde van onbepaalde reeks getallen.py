def gemiddelde():
    som = 0
    aantalIngevoerd = 0

    while True:
        invoer = int(input("Geef een getal:    "))

        if invoer == 0:
            break
        else:
            som += invoer
            aantalIngevoerd += 1

    gemiddeld = som/aantalIngevoerd

    print(gemiddeld)

gemiddelde()