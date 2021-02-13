class Human:
  def __init__(self, age, name):
    self.age = age
    self.name = name

class Student(Human):
  grades = []
  
  def add_grade(self, grade):
    self.grades.append(grade)
  
  def get_average_grade (self):
    return sum(self.grades) / len(self.grades) 
