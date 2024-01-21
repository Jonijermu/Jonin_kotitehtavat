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


# Sisäkkäiset kontrollirakenteet ja satunnaisuus
import random

random_number = random.randint(1,2)
print(f' Arvottu numero: {random_number}')

# pelin "asetukset"
player_count = 3
current_player = 1
dice_amount = 4

best_player = None
best_result = 0

#jokainen pelaaja suorittaa vuorollaan, aloitetaan pelaajasta 1
current_player = 1
while current_player <= player_count:
    result = 0 #silmälukujen summa ennen heittoja
    throw_count = 0 # iteraattori nopan heitoille
    # noppaa heitetään dice_amount - muuttujassa asetettu määrä
    while throw_count < dice_amount:
        dice = random.randint(1, 6)
        print(f'Pelaaja {current_player}, {throw_count+1}. heitto {dice}')
        result = result + dice
        throw_count += 1 # sama kuin throw_count = throw_count + 1
    print(f'Pelaajan {current_player} tulos: {result}')
    # testataan saatiinko uusi paras tulos, ja tallennetaan tavittessa
    # edellisen parhaan tuloksen tilalle, päivitetään samalla paras pelaaja
    if result > best_result:
        best_result = result
        best_player = f'pelaaja {current_player}'
        # jos tulos ei ole parempi, mutta on sama kuin edellinen paras tulos,
        #yhdistetään pelaajaan nimi edellisen parhaan pelaajan nimen lisäksi
        #samaan stringiin
    elif result == best_result:
        best_player = best_player + f' ja pelaaja {current_player}'
    current_player = current_player +1
print(f'paras tulos {best_result}, {best_player} ')

"""

# brreak-komento, "heittää" ulos aktiivisesta silmukasta, suoritus jatkuu
# kodinlohkon jälkeen

counter = 0
while True: # ikuinen silmukka
    print(f'laskuri eka {counter}')
    counter +=1
    if counter == 5:
        break # poistuu silmukan koodilohkosta samantien, allaoleva
        #ei tulostu
    print(f'laskuri toka {counter}')

