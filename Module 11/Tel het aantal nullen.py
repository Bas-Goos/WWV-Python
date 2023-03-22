def somNGetallen():
    aantalGetallen = int(input("Hoeveel getallen wilt u invoeren?   "))
    aantalNullen = 0

    for i in range(aantalGetallen):
        getal = int(input("Geef het getal dat je bij de som wilt optellen:  "))
        
        if getal == 0:
            aantalNullen += 1

    print(aantalNullen)

somNGetallen()