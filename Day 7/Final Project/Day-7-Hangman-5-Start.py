#Step 5

import random
from hangman_art import *
from hangman_words import *

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while True:
  guess = input("Guess a letter: ").lower()

  #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
  if guess in display:
    print(f"You have already guessed the letter {guess}")

  #Check guessed letter
  for position in range(word_length):
    for i in display:
        letter = chosen_word[position]
        if letter == guess:
          display[position] = letter

    #Check if user is wrong.
  if guess not in chosen_word:
    #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    print(f"You guessed the letter {guess} that is not in the word. You lose a life")
    lives -= 1
    if lives == 0:
      print("You lose.")
      print(f"{' '.join(display)}")
      print(stages[lives])
      break

    #Check if user has got all letters.
  if not i == "_" and lives > 0:
    print(f"{' '.join(display)}")
    print("You win.")
    print(stages[lives])
    break

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
  print(f"{' '.join(display)}")
  #Join all the elements in the list and turn it into a String.
  print(stages[lives])
