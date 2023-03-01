def gelijkeGetallen():
    getal1 = int(input("Geef getal 1:   "))
    getal2 = int(input("Geef getal 2:   "))
    getal3 = int(input("Geef getal 3:   "))

    if getal1 == getal2 == getal3:
        print(3)
    elif getal1 == getal2 or getal2 == getal3 or getal1 == getal3:
        print(2)
    else:
        print(0)

gelijkeGetallen()