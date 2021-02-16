arr = []
for i in range(11):
  arr.append(i*i)
print(arr)

###

numbers = [i**2 for i in range(1,11)]
print(numbers)

#######################

# wrapperis
def repeat_two_times(function):
  def inner(*args,**kwargs):
    function(*args, **kwargs)
    function(*args, **kwargs)
  return inner

@repeat_two_times
def function():
  print("hello")

function()

#######################

import random

def generate_random_numbers(ammount,start,end):
  for i in range(ammount):
    print(random.uniform(start, end))

generate_random_numbers(ammount=5, start=2.5, end=7.2)

###

import random

def generate_random_numbers(ammount,start,end):
  print([random.uniform(start, end) for i in range(ammount)])
  
generate_random_numbers(ammount=5, start=2.5, end=7.2)

###

import random

def generate_random_numbers(ammount,start,end):
  print(*[random.uniform(start, end) for i in range(ammount)], sep='\n')
  
generate_random_numbers(ammount=5, start=2.5, end=7.2)


#######################



#######################



#######################
