def rekeningNummers():
    adres = int(input("Geef een rekeningnummer: "))

    controleGetal2 = adres % 97
    if controleGetal2 < 10:
        controleGetal2 = "0" + str(controleGetal2)
        print(str(controleGetal2)+str(controleGetal2))
    controleGetal1 = 98 - (int(str(controleGetal2) + str(controleGetal2) + "111400")%97)



    print("BE", controleGetal1, adres, controleGetal2)

rekeningNummers()