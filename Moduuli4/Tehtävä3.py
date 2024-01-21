luku = float(input("Anna luku(tyhjä merkkijono lopettaa)" ))
while luku > 0:
    if luku == " ":
        break
    luku = float(input("Anna luku(tyhjä merkkijono lopettaa)"))
    if luku:
        pienin = float(min(luku))
        suurin = float(max(luku))
print(f'pienin numero: {pienin}, suurin numero: {suurin}')

