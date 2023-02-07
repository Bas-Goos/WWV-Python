def maandEnDagPasen():
    jaartal = int(input("Geef een jaartal:  "))

    a = jaartal % 19
    b = jaartal // 100
    c = jaartal % 100
    d = b // 4
    e = b % 4
    f = (b+8) // 25
    g = (b-f+1) // 3
    h = (19*a+b-d-g+15) % 30
    i = c // 4
    k = c % 4
    l = (32+2*e+2*i-h-k) % 7
    m = (a+11*h+22*l) // 451
    