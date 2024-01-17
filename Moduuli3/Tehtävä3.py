# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
# Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.
sukupuoli = input('Anna sukupuolesi Mies/Nainen: ')
hemoglobiiini = float(input('Mikä on hemoglobiinisi: '))
if sukupuoli == "mies":
    if 134 <= hemoglobiiini <= 195:
        print("Normaali verenpaine")
    elif hemoglobiini > 134:
        print('Alhainen hemoglobiini')
    else hemoglobiini < 195:
        print('Korkea hemoglobiini')







#ikä = int(input("Anna ikä: "))
#if 15<=ikä<18:
#   paino = float(input("Anna paino (kg): "))
#if (ikä>=18 or ikä>=15 and paino>=55):
#    print("Lääkkeen käyttö on sallittua.")
#else:
#    print("Lääkettä ei saa käyttää.")