import random
from hangman_art import *
from hangman_words import *

print(logo)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

while True:
  guess = input("Guess a letter: ").lower()

  if guess in display:
    print(f"You have already guessed the letter {guess}")

  for position in range(word_length):
    for i in display:
        letter = chosen_word[position]
        if letter == guess:
          display[position] = letter

  if guess not in chosen_word:
    print(f"You guessed the letter {guess} that is not in the word. You lose a life")
    lives -= 1
    if lives == 0:
      print("You lose.")
      print(f"{' '.join(display)}")
      print(stages[lives])
      break

  if not i == "_" and lives > 0:
    print(f"{' '.join(display)}")
    print("You win.")
    print(stages[lives])
    break

  print(f"{' '.join(display)}")
  print(stages[lives])
