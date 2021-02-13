count = int(input("Enter the ammount of numbers: "))
numbers = set()

for i in range(count):
  num = int(input("Enter number: "))
  numbers.add(num)

print(numbers)

##############


def create_set_elements(count):
  _set = set()
  for i in range(count):
    val = str(input("Enter string: "))
    _set.add(val)
  return _set

count1 = int(input("Ammount of elements in set: "))
elements1 = create_set_elements(count1)

count2 = int(input("Ammount of elements in set: "))  
elements2 = create_set_elements(count2)

isSecondSetSubsetOfFirstSet = elements2.issubset(elements1)
print(f"Is second set a subset of first set: {isSecondSetSubsetOfFirstSet}")

##############


def create_set_elements(count):
  _set = set()
  for i in range(count):
    val = str(input("Enter string: "))
    _set.add(val)
  return _set

count1 = int(input("Ammount of elements in set: "))
elements1 = create_set_elements(count1)

count2 = int(input("Ammount of elements in set: "))  
elements2 = create_set_elements(count2)

print(f"Union : {elements1.union(elements2)}")
print(f"Difference : {elements1.difference(elements2)}")
print(f"Intersection : {elements1.intersection(elements2)}")

##############

tuple1 = ((1, 153, 12), (214, 12, 215), (41, 856, 15), (42, 119, 9))
_list = []
for elem in tuple1:
  _list.append(sum(elem)/3)

print(_list)

##############

tuple1 = (321, 124124, 214, 2141, 21421, 2525, 25235)
print(tuple1)
print(tuple1[:-1])

##############

def create_set_elements():
  _set = set()
  for i in range(10):
    val = int(input("Enter number: "))
    _set.add(val)
  return _set

elements1 = create_set_elements()
print(elements1)

elements2 = set()
for i in elements1:
  if i % 3 != 0:
    elements2.add(i)
print(elements2)


##############

def calcSol (a,b,c):
  disc = b**2 - (4*a*c)
  sol1 = (-b - (disc**0.5))/(2*a)
  sol2 = (-b + (disc**0.5))/(2*a)
  res = (sol1, sol2)
  print(res)
  return res

coefA = int(input("Enter coeficient a: "))
coefB = int(input("Enter coeficient b: "))
coefC = int(input("Enter coeficient c: "))

result = calcSol(coefA, coefA, coefC)
print(f"Solution: {result}")
# not working.. code copy-paste, but giving ((x1,x2),(x3,x4)) not (x1,x2)

##############
