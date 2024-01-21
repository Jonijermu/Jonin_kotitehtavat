pituus = float(input('Anna pituus tuumissa: '))
cm = pituus * 2.54
while pituus > 0:
    if pituus < 0:
        break
    print(f'Pituutesi cm on: {cm}')
    pituus = float(input('Anna pituus tuumissa: '))
print('Annoit negatiivisen luvun ohjelma seis')



