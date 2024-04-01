import random

class Car:
    def __init__(self, license, top_speed):
        self.license = license
        self.top_speed = top_speed
        self.travel = 0

    def drive(self, hour):
        self.travel += self.top_speed * hour

    def tiedot(self):
        print(self.travel)


class ElectricCar(Car):

    def __init__(self, license, top_speed, battery):
        super().__init__(license, top_speed)
        self.battery = battery


class Gasoline(Car):
    def __init__(self, license, top_speed, tank_size):
        super().__init__(license, top_speed)
        self.tank_size = tank_size

electric_car = ElectricCar('ABC-15', 180, 52.5)
gasoline_car = Gasoline('ACD-123', 165, 32.3)

electric_car.drive(3)
gasoline_car.drive(3)

electric_car.tiedot()
gasoline_car.tiedot()

