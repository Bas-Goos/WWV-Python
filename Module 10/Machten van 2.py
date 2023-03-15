def kwadratenVan2():
    N = int(input("Geef een natuurlijk getal:   "))
    k = 0

    while 2**(k+1) <= N:
        k += 1
    
    print(k, 2**k)

kwadratenVan2()