import random

class Car:

    def __init__(self,license, top_speed, current_speed=0, travel_distance=0):
        self.license = license
        self.top_speed = top_speed
        self.current_speed = current_speed
        self.travel_distance = travel_distance

    def accelerate(self, speed_change):
        if speed_change > 0:
            self.current_speed = min(self.current_speed + speed_change, self.top_speed)
        elif speed_change < 0:
            self.current_speed = max(self.current_speed + speed_change, 0)

    def distance(self, travel_time):
        travel_distance = self.current_speed * travel_time
        self.travel_distance += travel_distance


cars = []

for i in range(1,11):
    license = 'ABC-' + str(i)
    top_speed = random.randint(100,200)
    car = Car(license, top_speed)
    cars.append(car)

the_race = True
while the_race:
    for car in cars:
        accelerate = random.randint(-10, 15)
        car.accelerate(accelerate)
        car.distance(1)
        if car.travel_distance >= 10000:
            the_race = False
            break


sorted_cars = sorted(cars, key=lambda x: x.travel_distance, reverse=True)

print("Autokilpailun tulokset:")
print("-------------------------------------------------")
print("| Rekisteritunnus | Huippunopeus | Matka (km) |")
print("-------------------------------------------------")
for car in sorted_cars:
    print(f"| {car.license:^15} | {car.top_speed:^13} | {car.travel_distance:^11.2f} |")
print("-------------------------------------------------")


