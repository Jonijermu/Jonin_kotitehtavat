class School:
    def __init__(self,name):
        self.name = name

school1 = School('Metropolia')
school2 = School('roskaHaaga')

class students:
    def __init__(self, name, School):
        self.name = name
        self.school =School

student1 = students('Renault', school1)
student2 = students('nönnö', school2)

print(f'{student1.name} {student1.school.name}')
print(f'{student2.name} {student2.school.name}')






