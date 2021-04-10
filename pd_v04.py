# No saraksta tiek nejauši izvēlēts kāds vārds. Lietotājam burtu vietā tiek parādītas svītriņas. Lietotājam ir iespēja minēt vārda burtus, kamēr ‘karatavas’ zīmējums nav pabeigts. Ja lietotāja minētais burts ir atrodams vārdā, tad svītriņu vietā parādās atbilstošs burts, ja lietotais kļūdās, tad ‘karatavas’ zīmējums tiek papildināts, lietotājam ir iespēja kļūdīties 6 reizes. Spēle beidzās līdz lietotājs uzmin visus vārda burtus vai kļūdās 6 reizes.

import random

def revealCharacters(word, characters):
  hiddenWord = list(word)
  for i,c in enumerate(word):
    if c not in characters:
      hiddenWord[i] = "-"
  return "".join(hiddenWord)

def validateInput(character, guessedCharacters):
  if character in guessedCharacters:
    print(f"Already tried with '{character}' - pick another!")
  elif character.isdigit():
    print(f"'{character}' is a digit, not a character - pick a character!")
  elif len(character) == 0:
    print("Empty space is not a character - pick a character!")
  else:
    guessedCharacters.append(character)
  return guessedCharacters

doLoopMenu = True
dictionary = ['apple','tomato','potato','banana','pear']
gallows = ["\n |--|\n    |\n    |\n    |\n    |\n    |\n",
          "\n |--|\n O  |\n    |\n    |\n    |\n    |\n",
          "\n |--|\n O  |\n |  |\n    |\n    |\n    |\n",
          "\n |--|\n O  |\n |  |\n |  |\n    |\n    |\n",
          "\n |--|\n O  |\n |  |\n/|  |\n    |\n    |\n",
          "\n |--|\n O  |\n |  |\n/|\ |\n    |\n    |\n",
          "\n |--|\n O  |\n |  |\n/|\ |\n/   |\n    |\n",
          "\n |--|\n O  |\n |  |\n/|\ |\n/ \ |\n    |\n"]

while doLoopMenu:
  print("Enter 1 to play hangman, 2 to add a new word, 3 to quit program")
  choice = str(input("Enter number: "))
  
  if choice == "1":
    doLoopGuess = True
    secretWord = random.choice(dictionary)
    mistakes = 0
    guessedCharacters = []
    while doLoopGuess:

      if mistakes > 6:
        print("You lose!\n=========\n")
        break
      
      if secretWord == revealCharacters(secretWord,guessedCharacters):
        print("You win!\n=========\n")
        break

      print(f"\n=========\n\nGuessed letters: {guessedCharacters}")

      character = str(input("Enter letter: "))
      guessedCharacters = validateInput(character,guessedCharacters)  
      if character not in secretWord:
        mistakes += 1

      print(f"Word: {revealCharacters(secretWord,guessedCharacters)}")

      print(gallows[mistakes])
    
  elif choice == "2":
    word = str(input("Enter new word: "))

    if word in dictionary:
      print(f"Word '{word}' already exists in dictionary")

    dictionary.append(word)
    print(f"Added {word}\n")

  elif choice == "3":
    doLoopMenu = False

  else:
    print("Unknown command!\n")
