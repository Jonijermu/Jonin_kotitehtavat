class Hissi:
    def __init__(self, alinkerros = 0, ylinkerros = 5):
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


hissi1 = Hissi()

hissi1.siirry_kerrokseen(5)
hissi1.siirry_kerrokseen(0)
