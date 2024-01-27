min_luku = None
max_luku = None

while True:
    syote = input("Syötä luku (tyhjä merkkijono lopettaa): ")

    if syote == "":
        break
    try:
        luku = int(syote)
        if min_luku is None or luku < min_luku:
            min_luku = luku
        if max_luku is None or luku > max_luku:
            max_luku = luku
    except ValueError:
        print("Virhe: Syötteen tulee olla kokonaisluku.")

if min_luku is not None and max_luku is not None:
    print(f"Pienin luku: {min_luku}")
    print(f"Suurin luku: {max_luku}")
else:
    print("Et syöttänyt yhtään kelvollista lukua.")


