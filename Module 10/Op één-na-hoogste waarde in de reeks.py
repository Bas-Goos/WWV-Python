def tweedeHoogste():
    hoogste = 0
    voorHoogste = 0

    while True:
        invoer = int(input("Geef een getal: "))
        if invoer == 0:
            break
        if invoer > hoogste:
            voorHoogste = hoogste
            hoogste = invoer
        if invoer < hoogste and invoer > voorHoogste:
            voorHoogste = invoer

    print(voorHoogste)

tweedeHoogste()