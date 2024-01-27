pituus = float(input('Anna pituus tuumissa: '))
cm = pituus * 2.54
while cm > 0:
    if cm < 0:
        break
    print(f'Pituutesi cm on: {cm} ')
    pituus = float(input('Anna pituus tuumissa: '))
    cm = pituus *2.54
print('Annoit negatiivisen luvun ohjelma seis')



