def calculate(number1, operator, number2):

  if number1.isnumeric() != True or number2.isnumeric() != True:
    print("Please enter numbers, not letters")
    return
  if number2 == "0":
    print("Can't divide by 0")
    return

  result = 0
  number1 = int(number1)
  number2 = int(number2)
  if operator == "+":
    result = number1 + number2
  elif operator == "-":
    result = number1 - number2
  elif operator == "/":
    result = number1 / number2
  elif operator == "*":
    result = number1 * number2
  else:
    print("Not recognized operator")
    return

  print(f"{number1} {operator} {number2} = {result}")

number1 = str(input("Enter number: "))
operator = str(input("Enter operator: "))
number2 = str(input("Enter number: "))
calculate(number1, operator, number2)

#################################

try:
  number1 = float(input("Enter number: "))
  operator = str(input("Enter operator: "))
  number2 = float(input("Enter number: "))
except:
    print("Please enter numbers, not letters")
    quit()

result = 0
if operator == "+":
  result = number1 + number2
elif operator == "-":
  result = number1 - number2
elif operator == "/":
  if number2 == 0:
    print("Cannot divide by 0")
    quit
  else:
    result = number1 / number2
elif operator == "*":
  result = number1 * number2
else:
  print("Not recognized operator")
  quit()

print(f"{number1} {operator} {number2} = {result}")

#################################

def create_items(count):
  _set = set()
  for i in range(count):
    val = int(input("Add number: "))
    _set.add(val)
  return _set

def remove_even_numbers(items):
  _set = set()
  for i in items:
    if i % 2 != 0:
      _set.add(i)
  return _set

items = create_items(5)
print(items)

itemsOdd = remove_even_numbers(items)
print(itemsOdd)

#################################

import random

def generate_random_numbers(count,min,max):
  numbers = []
  for i in range(count):
    numbers.append(random.randint(min, max))
  return numbers

items = generate_random_numbers(3, 0, 10)
print(items)

#################################

import random

class Car:
  max_fuel = 50;
  def __init__(self,model, regNumber):
    self.model = model
    self.regNumber = regNumber
    self.fuel = 0
    self.max_fuel = 50
    self.engineStarted = False
    self.passengers = {
      "front-left":None,
      "front-right":None,
      "back-left":None,
      "back-right":None,
    }

  def fuel_car(self):
    self.fuel = self.max_fuel
    print("Fuel tank is full now")

  def start_engine(self):
    success = bool(random.getrandbits(1))
    if success:
      self.engineStarted = True
      print("Engine started!")
    else:
      print("Engine did not started")
    
  def add_passenger(self, seating, passengerName):
    self.passengers[seating] = passengerName
    print(f"Added {passengerName}")
  
  def print_passengers(self):
    # code by Kristaps, but non-commented code is much cooler
    #for p in self.passengers:
    #  print(f"{p} : {self.passengers[p]}")
    for seat, passenger in self.passengers.items():
      print(f"{seat} : {passenger}")

car = Car("Volvo", "LV-0000")
car.fuel_car()
car.add_passenger("front-left","Max")
car.add_passenger("back-right","Alex")
car.print_passengers()

#################################
