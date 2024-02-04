import random

def nopan_silmaluku():
    print(random.randint(1,6))
    return

nopan_silmaluku()

def main():
    silmaluku = 0
    heitto = 0

    while silmaluku != 6:
        silmaluku = random.randint(1,6)
        heitto += 1
        print(f'Monesko heitto: {heitto}, Sait luvun: {silmaluku}')

    print('sait kutosen')
main()