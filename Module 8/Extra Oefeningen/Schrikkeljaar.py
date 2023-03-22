def schrikkeljaar():
    jaar = int(input("Geef een jaartal: "))

    if jaar % 400 == 0:
        print('SCHRIKKELJAAR')
    elif jaar % 100 == 0:
        print('GEEN SCHRIKKELJAAR')
    elif jaar % 4 == 0:
        print('SCHRIKKELJAAR')
    else:
        print('GEEN SCHRIKKELJAAR')

schrikkeljaar()