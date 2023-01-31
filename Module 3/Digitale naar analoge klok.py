def naarAnaloog():
    uren = int(input("Geef het aantal uren: "))
    minuten = int(input("Geef het aantal minuten:   "))

    if uren >= 12:
        uren -= 12
    
    graden = int((uren*30) + (minuten/2))

    print(graden)

naarAnaloog()