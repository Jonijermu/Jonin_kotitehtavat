
class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print("Nimi:", self.nimi)
class Kirja(Julkaisu):
    def __init__(self,nimi, kirjailija, sivumäärä):
        super().__init__(nimi)
        self.kirjailija = kirjailija
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print('kirjailija: ', self.kirjailija)
        print('Sivumäärä:',self.sivumäärä)

class Lehti(Julkaisu):
    def __init__(self,nimi, päätoimittaja):
        super().__init__(nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print('Päätoimittaja:',self.päätoimittaja)


lehti1 = Lehti("Aku Ankka", "Aki Hyyppä")
kirja1 = Kirja("Hytti nro 6", 'Rosa Liksom', 200)

kirja1.tulosta_tiedot()
lehti1.tulosta_tiedot()
