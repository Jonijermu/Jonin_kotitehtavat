height = input("suorakulmion korkeus?: ")
widht = input("suorakulmion leveys?: ")
area = float(height) * float(widht)
print("Pinta-ala: " + str(area))
piiri = float(height) * 2 + float(widht) * 2
print(f"Pinta-ala: {area}, Piiri: {piiri}" )