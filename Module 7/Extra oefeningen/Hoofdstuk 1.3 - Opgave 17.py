def gradenKlok():
    tijdstip1 = int(input("Geef het uur waarop de wijzer staat:   "))
    urenVerder = int(input("Geef het aantal uur dat de klok verder draait:  "))

    # Bereken op welk uur de wijzer staat na het passeren van dat aantal uur.
    tijdstip2 = (tijdstip1+urenVerder)%12
    graden = tijdstip2*30

    if graden >= 180:
        graden = 360-graden

    print(graden)

gradenKlok()