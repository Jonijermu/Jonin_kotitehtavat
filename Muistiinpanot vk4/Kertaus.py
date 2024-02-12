#import math
#print(f'{math.pi:10.2f}')


#nimi = input('Anna nimesi: ')
#while True:
#    if nimi != "James":
#        nimi = input('Anna nimesi uudelleen:')
#    else:
#        break
#print(f'hei {nimi}')


#eka = 1
#while eka <= 5:
#    toka = 1
#    while toka <= 5:
#        print(f'{eka} * {toka} = {eka * toka}')
#        toka = toka + 1
#    eka = eka + 1

#lista1 = [1, 5, 'juha', 3.14, [2, 5], (1,2,8), {'eka':4, 'toka': False}]
#print(lista1[3::-1])
#print('juha' in lista1)
#lista1.append(100)
#print(lista1)
#for x in range(8):
#    print('Moi')

#monikko = (1,5,10)
#eka, toka, kolmas = monikko
#print(eka)

#def erotus(luku1, luku2, ero):
#    ero = luku1 - luku2
#    return ero
#
#luku1 = float(input('anna ensimmäinen numero:'))
#luku2 = float(input('anna toinen numero: '))
#print(ero)

"""""
def toinen(lista):
    toinen = lista[1]
    return toinen

l1 = [1,4,6,8,9]
palautus = toinen(l1)
print(palautus)


def anna_nimi(sanakirja):
    palautus = sanakirja ['nimi']
    return palautus

sanak = {'nimi': 'jukka', 'ikä':20, 'ammatti': 'inssi'}
sanak2 = {'nimi': 'Jussi', 'ikä':30, 'ammatti': 'lääkäri'}

palaut = anna_nimi(sanak)
print(palaut)

def not_even(list):
    tyhlist = []
    for x in luvut:
        if x % 2 != 0:
            tyhlist.append(x)
    return tyhlist

luvut = [12, 5, 21, 4, 8, 0 ,11]
parit_list = not_even(luvut)
print(f'alkuperäiset luvut: {luvut}')
print(f'parittomat luvut: {parit_list}')


def douple(nums):
    tyhlist = []
    for x in nums:
        tyhlist.append(x*2)
    return tyhlist


luvut = [12, 5, 21, 4, 8, 0, 11]
parit_list = douple(nums)
print(f'alkuperäiset luvut: {luvut}')
print(f'parittomat luvut: {parit_list}')

"""

def operate(lista, rajat):
    tyhj = []
    for x in lista:
        if rajat[0] < x < rajat[1]:
            tyhj.append(x)
    return sum(tyhj)


list = [15, 1, 8, 18, 33, 1, 2]
borders = (0,9)
result = operate(list, borders)
print(f'{result}')


