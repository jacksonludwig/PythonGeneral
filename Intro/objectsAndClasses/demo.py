from Student import *


student1 = Student("john", "123 abc street", 19, 3.5, "Computer Science", 0)
student2 = Student("jackson", "3242 abc street", 19, 2.5, "Math", 1)

print(student1.name)
print(student1.major)
print(student1.on_honor_roll())

print(student1.reverse_name())
print(student2.reverse_name())
