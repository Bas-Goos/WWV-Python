def digitaleKlok():
    minSindsNacht = int(input("Geef het aantal minuten sinds middernacht:   "))

    if minSindsNacht >= 1440:
        minSindsNacht -= 1440
    
    uren = minSindsNacht // 60
    minuten = minSindsNacht % 60

    print(uren, minuten)

digitaleKlok()