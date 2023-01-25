def eeuw():
    jaartal = int(input("Geef een jaartal in:   "))

    eeuwMin1 = jaartal//100
    eeuw = eeuwMin1 + 1

    print(eeuw) 

eeuw()