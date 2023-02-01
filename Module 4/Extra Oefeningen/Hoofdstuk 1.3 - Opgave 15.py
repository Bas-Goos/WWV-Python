def geldNaarBriefjes():
    geld = int(input("Geef een bedrag (in euro):    "))

    vijftig = geld // 50
    geld = geld % 50

    twintig = geld // 20
    geld = geld % 20

    tien = geld // 10
    geld = geld % 10

    vijf = geld // 5
    geld = geld % 5

    twee = geld // 2
    geld = geld % 2

    een = geld

    print(vijftig, twintig, tien, vijf, twee, een)

geldNaarBriefjes()