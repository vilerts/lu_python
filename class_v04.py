input = [12, 21, 2154, 21, 21, 215, 21, 135, 13]
output = []
for item in input:
  output.append(item*2)

print(output)

##############

# Cristopher – 322414124
# Rebecca – 925232658
# Bob – 126521414

addressBook = {
  "Cristopher":322414124,
  "Rebecca":925232658,
  "Bob":126521414
}
print(addressBook)
addressBook.pop("Bob")
addressBook["Normund"] = "444444"
print(addressBook)

##############

count = int(input("Enter the ammount of numbers: "))
numbers = []
for i in range(count):
  num = int(input("Enter number: "))
  numbers.append(num)
print(numbers)

##############

count = int(input("Enter the ammount of numbers: "))
numbers = []
for i in range(count):
  num = int(input("Enter number: "))
  numbers.append(num)
print(numbers)
print(f"Maximum: {max(numbers)}")

##############

