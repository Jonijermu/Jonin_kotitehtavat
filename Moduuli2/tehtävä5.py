leviskä = float(input("Levisköjen määrä: "))
naula = float(input("Naulojen määrä: "))
luoti = float(input("Luotien määrä: "))

leviskä1 = float(int(leviskä) * 20 * 32 * 13.3 / 1000)
naula1  = float(int(naula) * 32 * 13.3 / 1000)
luoti1 = float(int(luoti) * 13.3/ 1000)

paino = leviskä1 + naula1 + luoti1
print(f"Kokonais paino on:{paino: .2f} kilogrammaa.")

# en osannu laittaa vastausta myös grammoina :(
