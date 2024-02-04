lentoasemat = {}
def lisää_lentoasema():
    icao_koodi = input('Anna lentoaseman ICAO koodi: ')
    lentoasema_nimi = input('Anna lentoasemna nimi: ')
    lentoasemat[icao_koodi] = lentoasema_nimi
    print(f'Lentoaseman nimi {lentoasema_nimi} ja ICAO-koodi {icao_koodi} lisätty.')

def lentoaseman_hakeminen():
    icao_koodi = input('Anna lentoaseman ICAO-koodi: ')
    lentoasema_nimi = lentoasemat.get(icao_koodi)
    if lentoasema_nimi:
        print(f"Lentoaseman {icao_koodi} nimi on {lentoasema_nimi}.")
    else:
        print('Ei löytynyt')

def main():
    while True:
        print("\n1. Lisää uusi lentoasema")
        print("2. Hae lentoaseman tiedot")
        print("3. Lopeta")

        valinta = input("Valitse toiminto (1/2/3): ")

        if valinta == "1":
            lisää_lentoasema()
        elif valinta == "2":
            lentoaseman_hakeminen()
        elif valinta == "3":
            print("Ohjelman suoritus päättyy.")
            break
        else:
            print("Virheellinen valinta. Valitse 1, 2 tai 3.")

main()