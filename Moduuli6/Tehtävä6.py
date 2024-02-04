import math
def pizza_laskuri(hinta, halkaisija):
    pinta_ala = (math.pi * (halkaisija/2)**2/ 10000)
    yksikkohinta = hinta / pinta_ala
    return yksikkohinta


pizza1 = float(input('Anna pizzan halkaisija: '))
hinta1 = float(input('anna pizzan hinta: '))
pizza2= float(input('Anna toisen pizzan halkaisija: '))
hinta2 = float(input('anna toisen pizzan hinta: '))

yksikkohinta1 = pizza_laskuri(hinta1, pizza1)
yksikkohinta2 = pizza_laskuri(hinta2, pizza2)

if yksikkohinta1 < yksikkohinta2:
    print('Ensimmäinen pizza oli halvempi:')
elif yksikkohinta1 > yksikkohinta2:
    print(f'toinen pizza oli halvempi')
elif yksikkohinta1 == yksikkohinta2:
    print('molemmat pizzat saman arvoisia')