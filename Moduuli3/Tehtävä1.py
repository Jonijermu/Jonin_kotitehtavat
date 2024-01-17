pituus = float(input("Kuinka pitkän kuhan sait? Anna tulos cm: "))
luku = pituus
if luku < 37:
    print('Laske takaisin veteen')
    print('kuha on: ' + str(37 - luku) + 'cm liian lyhyt')
if luku >= 37:
    print('jeejee saat pitää kuhan')
