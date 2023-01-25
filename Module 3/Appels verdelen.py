def Appelsverdelen():

    leerlingen = int(input("Hoeveel leerlingen zijn er? "))
    appels = int(input("Hoeveel appels zijn er?"))

    appelsPerLln = appels//leerlingen
    appelsOver = appels%leerlingen

    print(appelsPerLln)
    print(appelsOver)

Appelsverdelen()