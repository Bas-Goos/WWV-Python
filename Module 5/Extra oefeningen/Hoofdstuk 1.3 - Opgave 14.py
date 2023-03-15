def goniometrischeGetallen():
    xAB = float(input("Geef de lengte van AB:   "))
    xBC = float(input("Geef de lengte van BC:   "))

    xAC = ((xAB**2)+(xBC**2))**(1/2)

    sinus = round((xBC/xAC), 2)
    cosinus = round((xAB/xAC), 2)
    tangens = round((xBC/xAB), 2)

    print(sinus)
    print(cosinus)
    print(tangens)

goniometrischeGetallen()