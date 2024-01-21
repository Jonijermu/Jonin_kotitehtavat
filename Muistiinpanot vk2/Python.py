#nimi = ('james')
#print('nimesi on '+ nimi)
import random

#nimi = ('Joni')
#print(f'nimesi on {nimi}')
#import math
#math.pi = 3.14
#radius = float(input('anna säde:'));
#print(f'{math.pi*radius**2:.2f}')
#nimi = input('nimeni on: ')
#print(f'nimeni on {nimi}, "\U0001f600"')

#raha = 5
#ehto = raha > 2
#print(ehto)

#A = True
#B = True
#C = False
#D = False
#print(A and B)

#a = False
#b = False
#c = True

#d1 = (a and b) or c
#d2 =  a and (b or c)
#d3 = a and b or c
#print(d1)
#print(d2)
#print(d3)

#ikä = int(input("Anna ikä: "))
#if 15<=ikä<18:
#    paino = float(input("Anna paino (kg): "))
#if (ikä>=18 or (ikä>=15 and paino>=55)):
#    print("Lääkkeen käyttö on sallittua.")
#else:
#    print("Lääkettä ei saa käyttää.")

import random
noppa = random.randint(0, 1)
if noppa == 1:
     print('jeejee poeka')
else:
    print('jeejee tyttö')

    # pelin "asetukset"
    player_count = 3
    current_player = 1
    dice_amount = 4

    best_player = None
    best_result = 0

    # jokainen pelaaja suorittaa vuorollaan, aloitetaan pelaajasta 1
    current_player = 1
    while current_player <= player_count:
        result = 0  # silmälukujen summa ennen heittoja
        throw_count = 0  # iteraattori nopan heitoille
        # noppaa heitetään dice_amount - muuttujassa asetettu määrä
        while throw_count < dice_amount:
            dice = random.randint(1, 6)
            print(f'Pelaaja {current_player}, {throw_count + 1}. heitto {dice}')
            result = result + dice
            throw_count += 1  # sama kuin throw_count = throw_count + 1
        print(f'Pelaajan {current_player} tulos: {result}')
        # testataan saatiinko uusi paras tulos, ja tallennetaan tavittessa
        # edellisen parhaan tuloksen tilalle, päivitetään samalla paras pelaaja
        if result > best_result:
            best_result = result
            best_player = f'pelaaja {current_player}'
            # jos tulos ei ole parempi, mutta on sama kuin edellinen paras tulos,
            # yhdistetään pelaajaan nimi edellisen parhaan pelaajan nimen lisäksi
            # samaan stringiin
        elif result == best_result:
            best_player = best_player + f' ja pelaaja {current_player}'
        current_player = current_player + 1
    print(f'paras tulos {best_result}, {best_player} ')

    # while-silmukat (loopit)

    # jakolaskukone, jakaja ei voi olla nolla
    """
    num1 = float(input('anna jaettava numero: '))
    num2 = float(input('anna jakaja: '))
    while num2 == 0:
        print('Ei voi olla nolla.')
        num2 = float(input('Anna jakaja'))
    result = num1 / num2
    print(f"jakolasku tulos on {result}")


    # iteroiva silmukka (käytetään "laskuria" silmukan toistokertojen määrittely
    #i = 1  # iteraattori i
    i = int(input('mistä numerosta aloitetaan'))
    amount = int(input("kuinka monta numeroa tulostetaan"))
    offset = int(input('Anna numeroiden väli: '))
    max_number = amount * offset + i
    while i < max_number:
        print(f"numero on {i}")
        i = i + offset
    print(f'i;n lopullinen arvo silmukan jälkeen: {i}')

    #voit testata ehtolauseiden toiminta tulostamalla niiden arvoja
    print(i < i+1) # -> true
    """

    # Sisäkkäiset kontrollirakenteet ja satunnaisuus
 #   import random

 #   random_number = random.randint(1, 2)
 #   print(f' Arvottu numero: {random_number}')

