def zwarteSchaap():
    getal1 = int(input("Geef getal 1:   "))
    getal2 = int(input("Geef getal 2:   "))
    getal3 = int(input("Geef getal 3:   "))

    if getal1 == getal2:
        print(f"Het derde getal, nl. {str(getal3)} is het zwarte schaap.")
    elif getal2 == getal3:
        print(f"Het eerste getal, nl. {str(getal1)} is het zwarte schaap.")
    else:
        print(f"Het tweede getal, nl. {str(getal2)} is het zwarte schaap.")

zwarteSchaap()