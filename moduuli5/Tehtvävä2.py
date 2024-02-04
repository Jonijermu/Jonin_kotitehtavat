tyhlist = []
luvut = input('Syötä luku(tyhjä merkkijono lopettaa: ')
while luvut != "":
    tyhlist.append(luvut)
    luvut = input('Anna lisää lukuja(tyhjä merkkijono lopettaa: ')
tyhlist.sort(reverse=tyhlist, )
print(tyhlist)