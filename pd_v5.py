# Izveidot programmu, kurā būtu saraksts ar lietotājiem. Programmā ir izvēle, iegūt informāciju par konkrētu lietotāju, pievienot jaunu lietotāju, dzēst lietotāju no saraksta vai pārtraukt programmas izpildi.
# Izvēloties opciju “iegūt informāciju” tiek piedāvāta iespēja atrast lietotāju pēc e-pasta vai lietotājvārda. Ja lietotājs ir atrasts, tiek izvadīta visa zināma informācija par lietotāju, ja nav, tiek izvadīts atbilstošs paziņojums.
# Izvēloties opciju “pievienot lietotāju” sarakstam tiek pievienots lietotājs. Lai izveidotu lietotāju ir nepieciešams norādīt tā vārdu, lietotājvārdu, e-pastu. Automātiski tiek saglabāts laiks, kurā tika pievienots lietotājs.
# Izvēloties opciju “dzēst lietotāju” tiek piedāvāta iespēja atrast lietotāju pēc e-pasta vai lietotājvārda. Ja lietotājs ir atrasts, tas tiek dzēsts no saraksta, ja nav, tad tiek izvadīts atbilstošs paziņojums.
# Pēc izvēlētās darbības izpildīšanas lietotājam atkal tiek piedāvātas 4 opcijas.

from datetime import datetime

class User:
  def __init__(self, fullName, userName, email):
    self.fullName = fullName
    self.userName = userName
    self.email = email
    self.dateTimeCreated = datetime.now()

def getUser(userList, searchChoice): 
  foundUsers = None
  if searchChoice == "1":
    searchStringEmail = str(input("Enter e-mail: "))
    foundUsers = [x for x in userList if x.email == searchStringEmail]
  else:
    searchStringUsername = str(input("Enter username: "))
    foundUsers = [x for x in userList if x.userName == searchStringUsername]

  if len(foundUsers) == 1:
    return foundUsers[0]
  
  if len(foundUsers) > 1:
    print("Multiple users found")
  return None;

def searchUser(userList):
  if len(userList) == 0:
    print("User list empty!")
    return;

  print("Enter 1 to search by e-mail 2 to search by username")
  subChoice = str(input("Enter number: "))
  foundUser = getUser(userList=userList, searchChoice=subChoice)

  if foundUser is not None:
    print(f"  Full name: {foundUser.fullName}")
    print(f"  Username: {foundUser.userName}")
    print(f"  E-mail: {foundUser.email}")
    print(f"  Date and time added: {foundUser.dateTimeCreated}")
  else:
    print("User not found")

def addUser(userList):
  newFullName = str(input("  Full name: "))
  newUserName = str(input("  Username: "))
  newEmail = str(input("  E-mail: "))
  newUser = User(fullName=newFullName, userName=newUserName, email=newEmail)

  newUserList = userList
  newUserList.append(newUser)
  print("Added user")
  return newUserList

def removeUser(userList):
  if len(userList) == 0:
    print("User list empty!")
    return;
  
  print("Enter 1 to delete by e-mail 2 to delete by username")
  subChoice = str(input("Enter number: "))
  foundUser = getUser(userList=userList, searchChoice=subChoice)

  if foundUser is not None:
    userList.remove(foundUser)
    print("Removed user")
    return userList
  else:
    print("User not found")

  return userList

userList = []
doLoopMenu = True
while doLoopMenu:
  print("Enter 1 to print information about user, 2 to add new user, 3 to delete user, 4 to quit")
  choice = str(input("Enter number: "))
  
  if choice == "1":
    searchUser(userList=userList)
  elif choice == "2":
    userList = addUser(userList=userList)
  elif choice == "3":
    userList = removeUser(userList=userList)
  elif choice == "4":
    doLoopMenu = False
  else:
    print("Unknown command!\n")
  print("\n")
