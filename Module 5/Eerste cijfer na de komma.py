def cijferNaKomma():
    getal = float(input("Geef een kommagetal:   "))

    getal = getal * 10
    naKomma = int(getal%10)

    print(naKomma)

cijferNaKomma()