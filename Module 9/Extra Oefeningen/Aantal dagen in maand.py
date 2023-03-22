def dagInMaand():
    maand = int(input("Geef het nummer van de maand:    "))
    maandenMet31dagen = [1,3,5,7,8,10,12]
    maandenMet30dagen = [4,6,9,11]

    if maand == 2:
        dagenInMaand = 28
    if maand in maandenMet31dagen:
        dagenInMaand = 31
    if maand in maandenMet30dagen:
        dagenInMaand = 30

    print(dagenInMaand)

dagInMaand()