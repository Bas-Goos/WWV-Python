def somNGetallen():
    aantalGetallen = int(input("Hoeveel getallen wilt u invoeren?   "))
    somGetallen = 0

    for i in range(aantalGetallen):
        getal = int(input("Geef het getal dat je bij de som wilt optellen:  "))
        somGetallen += getal

    print(somGetallen)

somNGetallen()