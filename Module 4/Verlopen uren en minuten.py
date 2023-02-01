def digitaleKlok():
    secSindsNacht = int(input("Geef het aantal minuten sinds middernacht:   "))

    minSindsNacht = secSindsNacht // 60
    seconden = secSindsNacht % 60

    if minSindsNacht >= 1440:
        minSindsNacht -= 1440
    
    uren = minSindsNacht // 60
    minuten = minSindsNacht % 60

    print(f"{str(uren)}:{str(minuten)}:{str(seconden)}")

digitaleKlok()