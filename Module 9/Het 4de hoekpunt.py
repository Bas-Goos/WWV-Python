def hoekpunt4():
    x1 = int(input("Geef de x-waarde van hoekpunt 1:    "))
    y1 = int(input("Geef de y-waarde van hoekpunt 1:    "))
    x2 = int(input("Geef de x-waarde van hoekpunt 2:    "))
    y2 = int(input("Geef de y-waarde van hoekpunt 2:    "))
    x3 = int(input("Geef de x-waarde van hoekpunt 3:    "))
    y3 = int(input("Geef de y-waarde van hoekpunt 3:    "))

    if x1 == x2:
        x4 = x3
    elif x2 == x3:
        x4 = x1
    elif x1 == x3:
        x4 = x2
    
    
    if y1 == y2:
        y4 = y3
    elif y2 == y3:
        y4 = y1
    elif y1 == y3:
        y4 = y2

    print(x4)
    print(y4)

hoekpunt4()