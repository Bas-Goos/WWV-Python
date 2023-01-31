def weekdag():
    dag = int(input("Geef de dag van het jaar:  "))

    rest = (dag % 7) + 3

    if rest >= 7:
        rest -= 7
    
    print(rest)

weekdag()