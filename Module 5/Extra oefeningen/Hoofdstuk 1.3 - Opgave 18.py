def siNaarImperial():
    lengteCM = float(input("Geef de lengte van de persoon in cm:    "))

    inches = lengteCM/2.54
    
    # Splitsen van het totaal aantal inches naar feet en inches.

    feet = int(inches//12)
    inches -= (12*feet)

    print(feet, round(inches, 1))

siNaarImperial()
