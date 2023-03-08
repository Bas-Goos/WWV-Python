def AenB():
    x1 = float(input('Geef x1:    '))
    y1 = float(input('Geef y1:    '))
    x2 = float(input('Geef x2:    '))
    y2 = float(input('Geef y2:    '))

    # Rico berekenen
    a = (y2-y1)/(x2-x1)

    # b berekenen
    b = y1 - (a*x1)

    print(a, b)

AenB()