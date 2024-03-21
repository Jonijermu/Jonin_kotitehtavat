class Car:

    def __init__(self,license, top_speed, current_speed = 0, travel_distance = 0 ):
        self.license = license
        self.top_speed = top_speed
        self.current_speed = current_speed
        self.travel_distance = travel_distance

    def luodaan_uusi_auto(self):
        c1 = Car('ABC-123', 142)
        return c1


c1 = Car('', 0,)
c2 = Car('SJY-264', 0, 0,0 )
c3 = Car('PAS-296', 0, 0,0 )

c1 = c1.luodaan_uusi_auto()
print(f'Rekisteri tunnus: {c1.license}, huppunopeus: {c1.top_speed}km/h, tämän hetkinen nopeus: {c1.current_speed}kmh/, kuljettu matka: {c1.travel_distance}km')
