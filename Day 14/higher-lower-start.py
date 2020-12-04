import random
from art import logo, vs
from game_data import data
from replit import clear

#Get game will grab the index that I'm looking for
def getindex():
  return random.choice(data)

#Function/Command to print the list of random choice of array that I'm looking for. ----> DONE

#I need a compare function to decide whose followers are lesser and greater and accordingly add to the score.
#If the answer is right, I will add 1 else return the total score and say that the player loses.

#If I give the right answer, I will have to clear the console, increment the score and put a random index value for B again and shift the contents from 'Compare B' to 'A' in a while loop. The loop will break once I enter the wrong answer.

# index = random.choice(data)
# print(index['name'])
# print(index['follower_count'])
# print(index['description'])
# print(index['country'])
flag = True
while flag:
  print(logo)
  index = getindex()
  print(f"Compare A: {index['name']}, a {index['description']}, from {index['country']}")
  print(vs)
  index = getindex()
  print(f"Compare A: {index['name']}, a {index['description']}, from {index['country']}")
  choice = input("Who has more followers? Type 'A' or 'B':").upper()
  if choice == 'A':
    print('A')
    clear()
  elif choice == 'B':
    print('B')
    clear()
