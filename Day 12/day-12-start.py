from art import logo
import random

def level(a):
  if a == "easy":
    return 10
  elif a == "hard":
    return 5

def guess(n):
  global count
  while count >= 1:
    x = int(input("Make a guess: "))
    if x > n or x < n:
      count -=1
      if count != 0:
        highlow(x,n)
        print("Guess again")
        print(f"You have {count} attempts remaining to guess the number.")
    elif x == n:
      print(f"You got it! The answer is {x}")
  print("You've run out of guesses, you lose.")

def highlow(a, x):
  if a > x:
    print("Too high")
  elif a < x:
    print("Too low")


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1,100)
print(f"Pssst, the correct answer is {number}")
choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
count = level(choice)
print(f"You have {count} attempts remaining to guess the number.")
guess(number)
