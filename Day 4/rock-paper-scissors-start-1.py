import random

random.seed()

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
def rps(x):
  if x == 0:
    print(rock)
  elif x == 1:
    print(paper)
  elif x == 2:
    print(scissors)

choice = int(input(print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")))
rps(choice)
print("Computer chose: ")
comp = random.randint(0,2)
rps(comp)

if choice == comp:
  print("It's a draw")
if choice == 2:
  if comp == 1:
    print("You win")
  if comp == 0:
    print("You lose")
if choice == 1:
  if comp == 0:
    print("You win")
  if comp == 2:
    print("You lose")
if choice == 0:
  if comp == 1:
    print("You lose")
  if comp == 2:
    print("You win")
