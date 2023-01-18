def tijdTussen2():
    uur1 = int(input("Geef het eerste uur:  "))
    min1 = int(input("Geef de eerste minuten:   "))
    sec1 = int(input("Geef de eerste seconden:  "))

    uur2 = int(input("Geef het tweede uur:  "))
    min2 = int(input("Geef de tweede minuten:   "))
    sec2 = int(input("Geef de tweede seconden:  "))

    uurVerschil = uur2 - uur1
    minVerschil = min2 - min1
    secVerschil = sec2 - sec1

    uurNaarSec = uurVerschil * 3600
    minNaarSec = minVerschil * 60

    totaleSeconden = uurNaarSec + minNaarSec + secVerschil

    print(totaleSeconden)

tijdTussen2()