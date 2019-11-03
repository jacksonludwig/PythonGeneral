from objectsAndClasses.Person import Person


class Student(Person):

    def __init__(self, name, address, age, gpa, major, id_number):
        super().__init__(name, address)
        self.age = age
        self.gpa = gpa
        self.major = major
        self.id_number = id_number

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
