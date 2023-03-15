def kwadraten():
    N = int(input('Geef een natuurlijk getal:   '))
    i = 1
    getallenLijst = ""

    while i**2 <= N:
        getallenLijst = getallenLijst + " " + str(i**2)
        i += 1

    print(getallenLijst)

kwadraten()