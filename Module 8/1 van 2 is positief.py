def éénPositief():
    getal1 = int(input("Geef een getal: "))
    getal2 = int(input("Geef een ander getal:   "))

    positieve = negatieve = False

    if getal1 > 0 or getal2 > 0:
        positieve = True
    if getal1 < 0 or getal2 < 0:
        negatieve = True

    if negatieve == True and positieve == True:
        print('EXACT 1 POSITIEF')
    else:
        print('NIET VOLDAAN')

éénPositief()