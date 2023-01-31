def aankomstdag():
    afstandPerDag = int(input("Hoeveel afstand wordt er per dag afgelegd?   "))
    afstand = int(input("Hoeveel afstand moet er afgelegd worden?   "))

    rest = afstand % afstandPerDag

    if rest != 0:
        print((afstand//afstandPerDag)+1)
    elif rest == 0:
        print(afstand/afstandPerDag)

aankomstdag()