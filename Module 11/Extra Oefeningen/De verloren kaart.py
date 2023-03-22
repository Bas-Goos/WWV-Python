def verlorenKaart():
    aantalKaarten = int(input("Geef het aantal kaarten: "))
    kaartnummers = []

    for i in range(aantalKaarten):
        kaartnummers.append(int(input(f"Geef het kaartnummer van kaart {str(i+1)}:  ")))

    i = 1
    while i <= len(kaartnummers)+1:
        if i not in kaartnummers:
            print(i)
        i += 1
    
verlorenKaart()