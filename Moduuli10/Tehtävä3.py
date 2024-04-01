class Hissi:
    def __init__(self, alinkerros , ylinkerros):
        self.kerros = alinkerros
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros

    def siirry_kerrokseen(self, kohdekerros):
        while self.kerros != kohdekerros:
            if self.kerros < kohdekerros:
                self.kerros_up()
            else:
                self.kerros_down()


    def kerros_up(self):
        if self.kerros < self.ylinkerros:
            self.kerros += 1
            print(f'Kerroksessa: {self.kerros}')
        else:
            print('s')

    def kerros_down(self):
        if self.kerros > self.alinkerros:
            self.kerros -= 1
            print(f'Kerroksessa: {self.kerros}')
        else:
            print('a')

class Talo:
    def __init__(self, alinkerros , ylinkerros, hissi_nro):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.hissit = [Hissi(alinkerros, ylinkerros)for x in range(hissi_nro)]


    def aja_hissiä(self, hissin_numero, kohdekerros):
        if 0 <= hissin_numero <= len(self.hissit):
            self.hissit[hissin_numero].siirry_kerrokseen(kohdekerros)
        else:
            print('Hissiä ei ole')

    def fire_alarm(self):
        for i, hissi in enumerate(self.hissit):
            self.aja_hissiä(i +1, self.alinkerros)


talo1 = Talo(1, 10, 3)

talo1.aja_hissiä(2, 10)
talo1.aja_hissiä(1, 5)

talo1.fire_alarm()







