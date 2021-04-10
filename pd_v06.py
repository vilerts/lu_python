# 1. Izveidot sarakstu, kur ir skaitļi no 1 līdz 100, kas nedalās ar 3.
numbers = [i for i in range(1,101) if i%3==0]
print(numbers)


# 2. Ir dots tuple ar vārdiem (“Alex”, “Carl”, “Hannah”). Izveidot klasi Student, kurai ir atribūts name. Izveidot sarakstu ar Student klases objektiem.
class Student:
    def __init__ (self, name):
      self.name = name

items = ("Alex", "Carl", "Hannah")
students = []
for item in items:
  students.append(Student(name=item))

print([s.name for s in students])


# 3. Izveidot ģeneratora funkciju, kas ģenerē skaitļa reizinājumus ar skaitļiem no 0 līdz 10
multiplier = int(input("Enter number: "))
numbers = [i*multiplier for i in range(1,11)]
print(numbers)


# 4. Izveidot dekoratoru, kas izprintēs funckijas nosaukumu, kad tā tiks izsaukta
# wrapperis
def print_function_nme(function):
  def inner(*args,**kwargs):
    print(f"Executing: {function.__name__}")
    function(*args, **kwargs)
  return inner

@print_function_nme
def print_ok():
  print("Ok")

print_ok()


# 5. Izveidot ģeneratora funkciju, kas ģenerē pirmskaitļus (skaitļi kas dalās tikai ar 1 vai ar sevi, 0 un 1 nav pirmskaitļi).
def is_prime(num):
  if num == 0 or num == 1:
    return False
  for x in range(2, num):
    if num % x == 0:
      return False
  return True

primes = [i for i in range(1,100) if is_prime(i)]
print(primes)


# 6. Izveidot range() analogu, argumentu secībai nav nozīmes.
def my_range(*args):
  start = args[0]
  end = args[1]
  step = 1 
  if len(args) == 3 and args[2] != None:
    step = args[2]
  
  arr=[]
  counter = start
  while counter < end:
    arr.append(counter)
    counter += step
  return arr

print([i for i in my_range(1,10)])
print([i for i in my_range(1,11,3)])

