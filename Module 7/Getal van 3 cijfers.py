def getal3Cijfers():
    getal = int(input("Geef een getal:  "))

    if getal < 1000 and getal > 99:
        print('DRIE')
    else:
        print('NIET (!) DRIE')

getal3Cijfers()