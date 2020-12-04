import random
from art import logo, vs
from game_data import data
from replit import clear

#Get game index will grab the index from game_data
def getindex():
  return random.choice(data)

#Function/Command to print the list of random choice of array that I'm looking for.

#I need a compare function to decide whose followers are lesser and greater and accordingly add to the score.

def compare(choice, index1, index2):
  if choice == "A" and index1['follower_count'] > index2['follower_count']:
    return True
  if choice == "B" and index1['follower_count'] < index2['follower_count']:
    return True
  else:
    return False

#If I give the right answer, I will have to clear the console, increment the score and put a random index value for B again and shift the contents from 'Compare B' to 'A' in a while loop. The loop will break once I enter the wrong answer.

flag = False
score = 0

index1 = getindex()
index2 = getindex()

while True:
  print(logo)
  if flag:
    print(f"You're right! Current score: {score}")
  print(f"Compare A: {index1['name']}, a {index1['description']}, from {index1['country']}")
  print(vs)
  print(f"Against B: {index2['name']}, a {index2['description']}, from {index2['country']}")
  choice = input("Who has more followers? Type 'A' or 'B': ").upper()
  clear()
#If the answer is right, I will add 1 else return the total score and say that the player loses.
  if compare(choice, index1, index2):
    flag = True
    score += 1
    index1 = index2
    index2 = getindex()
  else:
    print(f"Sorry, that's wrong. Final score: {score}")
    break
