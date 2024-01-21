sukupuoli = input('Anna sukupuolesi Mies/Nainen: ')
hemoglobiini = float(input('Mikä on hemoglobiinisi: '))
if sukupuoli == "Mies":
    if 134 <= hemoglobiini <= 195:
        print("Normaali verenpaine")
    elif hemoglobiini < 134:
        print('Alhainen hemoglobiini')
    elif hemoglobiini > 195:
        print('Korkea hemoglobiini')
if sukupuoli == 'Nainen':
    if 117 <= hemoglobiini <= 175:
        print("Normaali verenpaine")
    elif hemoglobiini < 117:
        print('Alhainen hemoglobiini')
    elif hemoglobiini > 175:
        print('Korkea hemoglobiini')