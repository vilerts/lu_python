# 1. Izveidot programmu, kas prasa lietotājam ievadīt skaitli n, tad programma aprēķina n+nn+nnn
print("### Task 1 ###")
number1 = input("Enter number: ")
number2 = str(number1) + str(number1)
number3 = str(number1) + str(number1) + str(number1)
result = int(number1) + int(number2) + int(number3)
print(str(number1) + "+" + str(number2) + "+" + str(number2) + "=" + str(result))
print()

# 2. Izveidot programmu, kura prasa lietotājam ievadīt cilindra rādiusu un tā augstumu, tiek aprēķināts cilindra laukums un tilpums. Rezultāts tiek parādīts konsolē.
print("### Task 2 ###")
height = int(input("Enter height: "))
radius = int(input("Enter radius: "))
volume = 3.14 * radius * radius * height
area = 2 * (3.14 * radius * radius) + height * (2 * 3.14 * radius)
print("Volume: " + str(volume))
print("Area: " + str(area))
print()

# 3. Izveidot programmu, kura prasa lietotājam sekunžu skaitu. Sekundes tiek pārveidotas par “x hours y minutes z seconds” tipa tekstu. Rezultāts tiek parādīts konsolē.
print("### Task 3 ###")
secondsTotal = int(input("Enter seconds: "))
hours = int(secondsTotal / 60 / 60) 
minutes = int((secondsTotal - hours * 60 * 60) / 60)
seconds = secondsTotal - hours * 60 * 60 - minutes * 60
print(str(hours) + " hours " + str(minutes) + " minutes " + str(seconds) + " seconds ")
print()

# 4. Izveidot kalkulatoru. Programma prasa lietotājam ievadīt divus skaitļus. Ar šiem skaitļiem tiek veiktas operācijas (saskaitīšana, atņemšana, reizināšana, dalīšana). Rezultāts tiek parādīts konsolē.
print("### Task 4 ###")
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
print(str(n1) + "+" + str(n2) + "=" + str(n1+n2))
print(str(n1) + "-" + str(n2) + "=" + str(n1-n2))
print(str(n1) + "*" + str(n2) + "=" + str(n1*n2))
print(str(n1) + "/" + str(n2) + "=" + str(n1/n2))
print()

# 5. Zemniekam ir govis, cūkas un vistas. Govīm un cūkām ir pa 4 kājām, vistām – 2.
# Izveidot programmu, kas prasa lietotājam ievadīt cūku, govju un vistu skaitu. Tiek aprēķināts kopējais kāju daudzums. Rezultāts tiek izvadīts konsolē.
print("### Task 5 ###")
countPigs = int(input("Ammount of pigs: "))
countCows = int(input("Ammount of cows: "))
countChickens = int(input("Ammount of chickens: "))
legs = (countPigs * 4) + (countCows * 4) + (countChickens * 2)
print("Total ammount of legs: " + str(legs))
print()

# 6. Kāda valsts nolēma pāriet uz jaunu naudas sistēmu. Vecajā sistēmā bija trīs naudas vienības: dālderis, grasis, santīms. Naudas vērtības norādītas zemāk.
# 1 dālderis = 37 graši
# 1 grasis = 162 santīmi
# Jaunajā naudas sistēmā paliek tikai santīmi un dālderi. Santīms saglabā savu vērtību, bet 1 dālderis būs vienāds ar 100 santīmiem.
# Izveidot programmu, kas pārveidotu vecās sistēmas naudu uz jaunu. Lietotājam prasa ievadīt vecās sistēmas dālderus, grašus un santīmus. Tiek aprēķināts jaunās sistēmas dālderu un grašu daudzums. Rezultāts tiek parādīts konsolē.
print("### Task 6 ###")
oldDalderi = int(input("Dālderi: "))
oldGrasi = int(input("Graši: "))
oldSantimi = int(input("Santīmi: "))
newSantimiTotal = oldSantimi + (oldGrasi * 162) + (oldDalderi * 37 * 162)
newDalderi = int(newSantimiTotal / 100)
newSantimi = newSantimiTotal - (newDalderi * 100)
print("Jaunie dālderi: " + str(newDalderi))
print("Jaunie santīmi: " + str(newSantimi))
print()
#
# Comment: there is a mistate in 6th task description.
# "Tiek aprēķināts jaunās sistēmas dālderu un ___grašu___ daudzums."
#                                                 ^--- "santīmu"
#
