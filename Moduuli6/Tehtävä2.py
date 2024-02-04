import random

def main():
    tahko = int(input('Anna tahkojen määrä: '))
    maksimiluku = int(input('Syötä nopan maksimiluku'))

    silmaluku = 0
    heittokerrat = 0

    while silmaluku != maksimiluku:
        silmaluku = random.randint(1, tahko)
        heittokerrat += 1
        print(f"Heitto {heittokerrat}: {silmaluku}")
    print(f"Noppa näytti maksimisilmäluvun {maksimiluku}")

main()