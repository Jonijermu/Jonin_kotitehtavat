class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayHello(self):
        print(f'Hello olen {self.name} ja olen {self.age}.')

class Student(Human):
    def __init__(self, name, age, number):
        super().__init__(name, age)
        self.number = number

    def sayHello(self):
        super().sayHello()
        print(f'student number is {self.number}')



human1 = Student("Joni", 26, 1234567)
student1 = Student('Jaska', 20, 98765)

human1.sayHello()
student1.sayHello()