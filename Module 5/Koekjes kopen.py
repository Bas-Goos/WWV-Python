def kostPrijs():
    euroPrijs = int(input("Geef het gehele deel van de prijs:   "))
    centPrijs = int(input("Geef het decimale deel van de Prijs: "))
    koekjes = int(input("Geef het aantal koekjes:   "))

    prijsEuro = euroPrijs * koekjes
    prijsCent = centPrijs * koekjes
    prijsEuro += prijsCent // 100
    prijsCent -= (prijsCent // 100) * 100

    print(int(prijsEuro), int(prijsCent))
    
kostPrijs()