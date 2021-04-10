# 1. Apgriezt pozitīva skaitļa ciparu secību
num = str(input("Enter number: "))
newNum = "";
for i in num[::-1]:
  newNum += i
print(newNum)


# 2. Atrast cik skaitļi norādītajā intervālā dalās ar lietotāja norādīto dalītāju.
start = int(input("Start: "))
end = int(input("End: "))
divider = int(input("Divider: "))

count = 0
for i in range(start,end, divider):
  if(i % divider == 0):
    count += 1

print(f"{count} numbers between {start} and {end} can be divided by {divider}")


# 3. Aprēķināt skaitļu summu lietotāja norādītajā intervālā. Ja skaitlis dalās ar 13 vai dalās ar 4 un ir trīsciparu skaitlis, tad skaitlis nav jāpievieno summai, bet, ja skaitlis ir četrciparu skaitlis un dalās ar 7, un dalās ar 1000, tad summas skaitīšana ir jāpārtrauc.
start = int(input("Start: "))
end = int(input("End: "))

sum = 0
for i in range(start, end):
  if i % 13 == 0:
    continue
  if i % 4 == 0 and len(str(i)) == 3:
    continue
  if len(str(i)) == 4 and i % 7 == 0 and i % 1000 == 0:
    break
  sum += i

print(f"Sum: {sum}")


# 4. Izprintēt konsolē burtu ‘P’.
chars = "****n*   *n*   *n****n*n*n*n"
for i in chars:
  if(i == "n"):
    print("\n", end = '')
    continue
  print(i, end = '')


# 5. Atrast pozitīva skaitļa ciparu summu.
num = int(input("Enter number: "))
sum = 0
for i in str(num):
  sum += int(i)
print(sum)


# 6. Izveidot reizināšanas tabulu lietotāja ievadītam skaitlim.
num = int(input("Enter number: "))
for i in range(1,11):
  print(f"{num}x{i}={num*i}")


# 7. Atrast pāra skaitļa summu norādītājā intervālā.
start = int(input("Start: "))
end = int(input("End: "))

sum = 0
for i in range(start,end):
  if(i % 2 == 0):
    sum += i

print(f"Sum: {sum}")

# 8. Izveidot struktūru, kas norādītā piemērā:
num = int(input("Enter number: "))
for i in range(1,num + 1):
  print(str(i) * i)
