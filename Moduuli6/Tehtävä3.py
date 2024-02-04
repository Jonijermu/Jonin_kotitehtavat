
def gallons_to_litres(gallons):
        litra = gallons * 3.785
        return litra

while True:
    gallons = float(input("Anna määrä galloina (negatiivinen numero lopettaa): "))
    if gallons < 0:
        print('ohjelma lopetetaan')
        break

    litra = gallons_to_litres(gallons)
    print(f'Määrä galloina {gallons} on litroina {litra}')