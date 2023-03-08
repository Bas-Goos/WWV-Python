def bmi():
    m = float(input("Geef de massa in kg: "))
    l = float(input("Geef de lengte in meter:   "))

    # Bereken BMI
    BMI = round(m/(l**2),1)
    print(BMI)

bmi()