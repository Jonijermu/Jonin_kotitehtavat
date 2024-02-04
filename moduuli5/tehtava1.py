import random

throw_amount = int(input('Anna heittojen määrä: '))

silmaluvut = []
for _ in range(throw_amount):
    heitto = random.randint(1, 6)
    silmaluvut.append(heitto)
print(f'silmälukujen summa: {sum(silmaluvut)}')