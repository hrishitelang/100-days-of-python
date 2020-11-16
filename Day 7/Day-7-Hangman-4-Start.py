#Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#Set 'lives' to equal 6.
lives = 6
flag = 0
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while True:
  guess = input("Guess a letter: ").lower()
  #Check guessed letter
  for position in range(word_length):
    for i in display:
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
      #TODO-2: - If guess is not a letter in the chosen_word,
      #Then reduce 'lives' by 1.
      #If lives goes down to 0 then the game should stop and it should print "You lose."
  if guess not in chosen_word:
    lives -= 1
    #print(lives)
    if lives == 0:
      print("You lose.")
      break
        #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.


#Check if user has got all letters.
  if not i == "_" and lives > 0:
    print(f"{' '.join(display)}")
    print("You win.")
    print(stages[lives])
    break
    #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")
  print(stages[lives])
