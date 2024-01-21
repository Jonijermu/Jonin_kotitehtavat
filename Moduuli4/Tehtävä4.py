def main():
    numerot = []

    while True:
        syote = input("Syötä luku (tyhjä merkkijono lopettaa): ")

        # Tarkista, onko käyttäjä syöttänyt tyhjän merkkijonon
        if syote == "":
            break

        try:
            luku = float(syote)
            numerot.append(luku)
        except ValueError:
            print("Virhe: Syötteen tulee olla luku.")

    if numerot:
        # Tulosta pienin ja suurin luku
        pienin = min(numerot)
        suurin = max(numerot)
        print(f"Pienin luku: {pienin}")
        print(f"Suurin luku: {suurin}")
    else:
        print("Et syöttänyt yhtään lukua.")

if __name__ == "__main__":
    main()
