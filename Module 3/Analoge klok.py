def AnalogeKlok():
    gradenKleine = int(input("Geef de graden van de kleine wijzer:"))

    gradenGrote = (gradenKleine%30)*12

    print(gradenGrote)

AnalogeKlok()