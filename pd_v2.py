# Izveidot spēli “Akmens šķēres papīrīt’s”.
# Lietotājs ievada skaitli 1, 2 vai 3. Skaitlis 1 apzīmē akmeni, 2 – šķēres, 3 – papīru.
# Programma nejauši izvēlās akmeni, šķēres, vai papīru.
# Uz ekrāna tiek parādīts ko ir izvēlējies lietotājs, ko – dators.
# Ja lietotājs ir uzvarējis vienu reizi, lietotājam tiek piešķirts punkts, ja ir uzvarējis dators, punkts tie piešķirts datoram. Ja lietotājs un dators ir izvēlējušies vienādu elementu, punkts netiek piešķirts nevienam.
# Pēc katra mēģinājuma tiek parādīts lietotāja un datora punktu skaits.
# Spēle turpinās tiklīdz kāds, dators vai lietotājs, iegūst trīs punktus.

# implementation by teacher : https://pastebin.com/HQG6tGTr

import random

scoreHuman = 0
scoreComputer = 0
gameValues = {
  "1" : "Rock",
  "2" : "Paper",
  "3" : "Scissors"
}

# outcome Matrix
# User  Comput  Outc  Value (count numeric value of input)
# R(1)  R(1)    D     0
# R(1)  P(2)    C     -1 (1(Rock) minus 2(Paper) equals 1-2=-1 and computer wins)
# R(1)  S(3)    H     -2
# P(2)  R(1)    H     1
# P(2)  P(2)    D     0
# P(2)  S(3)    C     -1
# S(3)  R(1)    C     2
# S(3)  P(2)    H     1
# S(3)  S(3)    D     0
#
# tranformed outcome Matrix
# Value Winner
# -2    H
# -1    C
# 0     Draw
# 1     H
# 2     C
#
# in other words, if result is:
#   0, then DRAW
#   -2 or 1, then HUMAN win
#   -1 or 2, then COMPUTER win

while (scoreHuman != 3 and scoreComputer != 3):
  print("Enter 1 for Rock, 2 for Paper, 3 for Scissors")

  valuePlayer = str(input("Your turn: ")) 
  if(valuePlayer not in ["1","2","3"]):
    print("Unknown value, please try again! \n")
    continue

  valueComputer = str(random.randint(1,3))
  print(valuePlayer + " vs. " + valueComputer)

  resultValue = int(valuePlayer) - int(valueComputer)
  if (resultValue == 0):
    print("Draw")
  elif (resultValue == -2 or resultValue == 1):
    print("User wins this round.")
    scoreHuman += 1
  elif (resultValue == -1 or resultValue == 2):
    print("Computer wins this round.")
    scoreComputer += 1
  else:
    print("Unknow result value !?!?!")

  print(str(scoreHuman) + ":" + str(scoreComputer) + "\n")

if (scoreComputer == 3):
  print("Computer wins!")
else:
  print("Human wins!")
