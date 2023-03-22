def somFaculteiten():
    n = int(input("Geef een getal n:    "))
    totaleSom = 0

    for i in range(n):
        faculteit = 1
        for j in range(i+1):
            faculteit = faculteit*(j+1)
        totaleSom += faculteit
    
    print(totaleSom)

somFaculteiten()