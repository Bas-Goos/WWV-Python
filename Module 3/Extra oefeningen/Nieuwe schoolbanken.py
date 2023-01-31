def schoolbanken():
    llnA = int(input("Geef het aantal leerlingen in klas A: "))
    llnB = int(input("Geef het aantal leerlingen in klas B: "))
    llnC = int(input("Geef het aantal leerlingen in klas C: "))

    bankA = llnA // 2
    if llnA % 2 != 0:
        bankA += 1
    bankB = llnB // 2
    if llnB % 2 != 0:
        bankB += 1
    bankC = llnC // 2
    if llnC % 2 != 0:
        bankC += 1
    
    som = bankA + bankB + bankC

    print(som)

schoolbanken()