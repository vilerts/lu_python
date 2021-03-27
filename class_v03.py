number1 = int(input("Enter first number: "))
number2 = int(input("Enter first number: "))

if number1 > number2:
  number_biggest = number1
  number_smallest = number2
else:
  number_biggest = number2
  number_smallest = number1

for i in range(number_biggest):
  print(number_smallest)


##############

height = int(input("Enter the height of the pyramid: "))
rows = 2 *height - 1

for i in range(rows+1):
  if(i < height):
      print("*"*i)

  if(i == height):
      print("*"*height)

  if(i > height):
      print("*"*int(height*2 - i))

##############

numbers = []
for i in range(5):
  num = int(input("Enter number: "))
  numbers.append(num)

average = sum(numbers) / len(numbers)
print("Average: " + str(average))
  
count = 0
for i in numbers:
  if i > average:
      count += 1
print(f"{count} numbers are larger than average")
