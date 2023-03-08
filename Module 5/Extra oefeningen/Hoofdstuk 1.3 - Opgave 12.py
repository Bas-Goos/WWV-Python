def lengte():
    m = float(input("Geef het gewicht in kg:    "))
    bmi = float(input("Geef de BMI van de persoon:  "))

    # Berekenen lengte
    l = round(((m/bmi)**(1/2))*100,1)
    print(l)

lengte()