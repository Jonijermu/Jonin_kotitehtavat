class Animal:
    def __init__(self, species):
        self.species = species

    def speak(self):
        print("animal is making a sound")

class Dog(Animal):
    def __init__(self, species, breed):
        self.breed = breed
        super().__init__(species)

    def speak(self):
        print("animal is making a sound")

dog1 = Dog('dog', 'rotu')
dog1.speak()

