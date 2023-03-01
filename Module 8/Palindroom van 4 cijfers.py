def cijferPalindroom():
    getal = int(input("Geef een getal van 4 cijfers:    "))

    laatste2 = getal % 100
    eerste2 = getal // 100

    laatste = laatste2 % 10
    voorlaatste = laatste2 // 10

    omgewisseld = int(str(laatste) + str(voorlaatste))

    if omgewisseld == eerste2:
        print('EEN CIJFERPALINDROOM')
    else:
        print('GEEN CIJFERPALINDROOM')

cijferPalindroom()