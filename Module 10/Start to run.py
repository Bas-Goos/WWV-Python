def start2Run():
    xDag1 = int(input("Geef de afstand dat je kon lopen op dag 1:   "))
    xWedstrijd = int(input("Geef de afstand dat je moet lopen voor de wedstrijd:    "))
    Dagen = 1

    while xDag1*(1.1**Dagen) <= xWedstrijd:
        Dagen += 1

    print(Dagen+1)

start2Run()