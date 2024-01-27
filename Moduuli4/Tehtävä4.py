import random

arvattava_luku = random.randint(1, 10)
tries = 0

while True:
    arvaus = input("Anna luku väliltä 1-10: ")
    arvaus = int(arvaus)
    tries += 1
    if tries == 5:
        break
    if arvaus < arvattava_luku:
        print("Liian pieni arvaus.")
    elif arvaus > arvattava_luku:
        print("Liian suuri arvaus.")
    else:
        print("Oikein! Arvattu luku oli", arvattava_luku)
        print("Tarvitsit", tries, "arvauskertaa.")
        break