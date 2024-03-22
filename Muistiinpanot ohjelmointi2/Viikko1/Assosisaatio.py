class school:
    def __init__(self,name):
        self.name = name

school1 = school('Metropolia')
school2 = school('roskaHaaga')

class students:
    def __init__(self, name, school):
        self.name = name
        self.school = school

student1 = students('Renault', school1)
student2 = students('nönnö', school2)

print(f'{student1.name} {student1.school.name}')
print(f'{student2.name} {student2.school.name}')






