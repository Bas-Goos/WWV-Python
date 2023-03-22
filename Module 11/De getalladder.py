def getalladder():
    n = int(input("Geef een getal kleiner of gelijk aan 9:  "))
    trap = ""

    for i in range(n):
        trap = trap + str(i+1)
        print(trap)

getalladder()