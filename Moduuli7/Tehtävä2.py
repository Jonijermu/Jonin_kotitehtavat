nimet = set()
while True:
    nimi = input('Anna nimi(tyhjä merkkijono lopetaa): ')
    if nimi in nimet:
        print('Nimi on jo syötetty')
    else:
        print('uusi nimi')
        nimet.add(nimi)
    if nimi == "":
        break

print('Tässä nimet')
for name in nimet:
    print(name)