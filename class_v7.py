
print("\n".join(dir(str)))

#################################

import random

a = 5
print(type(a).__name__)

s = "h"
print(s.__class__.__name__)

r = random.Random()
print(type(r).__name__)


#################################

from fold_class_v7 import Cylinder

my_cylinder = Cylinder.Cylinder(radius=5,height=10)

print(my_cylinder.radius)
print(my_cylinder.height)
print(my_cylinder.area())
print(my_cylinder.volume())

#################################

from fold_class_v7 import Money

wallet = Money.Money2(euro=215)

print(wallet.usd())
print(wallet.rub())
print(wallet.gbp())
print(wallet.pln())

#################################

from fold_class_v7.Human import Human, Student

human = Human(name="Rebecca", age=40)
student = Student(name="Alex", age=21)
student.add_grade(7)
student.add_grade(10)
student.add_grade(8)
student.add_grade(2)
print(student.grades)
print(student.get_average_grade())

#################################
