age = 5
print(age)
age = 6
print(age + 2)
age_string = "seitsemän"
age_int = 6
print(age_int + 4)
print(age_string + " vuotta")

#Liukuluvut (Float)(ei ihan sama kuin desimaailuku)
depth = 10.0
width = 7
area = depth * width
print(area)

# Tyyppimuutokset
age_input = input("kuinka vanha olet?")
age_int = int(age_input) # 13
new_age = age_int + 1
print("vuoden päästä olen " + str(new_age) + " vuotta.")
# tai "f-stringillä"
print(f"vuoden päästä olen {new_age} vuotta.")

#boolean: totta vai tarua (pythonissa 1 tai 0)
isItTrue = True
print(isItTrue)

print(("_" * 80) + "\n Minun nimeni on Joni" + "\n" + ("_" * 80))

merkki = "_"
print(merkki*80)
print("minun nimeni on joni")
print(merkki*80)

# fahrenheit_str = input("Anna lämpötila Fahrenheit-asteina: ")
#fahrenheit = float(fahrenheit_str)
#celsius = (fahrenheit-32)*5/9
# print("Lämpötila Celsius-asteina: " + str(celsius))

# luku = 3
# print('mä asun osotteessa ' + str(luku))

# cm_str = int(input("Mikä on pituus tuumana, anna cm: "))
# tuuma_int = int(cm_str * 3)
# print("pituus tuumana: " + str(tuuma_int))

# tuuma = input("montako tuuma:\n")
# tuuma_int = int(tuuma)
# kerroin = 2.54
# sentti = kerroin * tuuma_int
# print(f'vastaus on senttinä: {sentti}')

import math
# from math import pi
munpi = math.pi
print(munpi)
print(f' {munpi: 2f}')
print(f' {munpi:10.5f}')

luku = 10
print(f' {luku:10d}')

luku = 11
if luku == 11:
    print("hello")
print("moi")
