##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

from art import logo
from replit import clear
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
  return random.choice(cards)

user_cards = []
computer_cards = []

def calculate_score(cardlist):
  if (cardlist == [11,10] or cardlist == [10,11]):
    return 0
  elif 11 in cardlist and sum(cardlist) > 21:
    for i in cardlist:
      if i == 11:
        cardlist.remove(i)
        cardlist.append(1)
        return sum(cardlist)
  else:
    return sum(cardlist)

choice1 = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

if choice1 == "y":
  flag = True
  clear()
  while flag:
    user_cards = []
    computer_cards = []
    print(logo)
    for i in range(2):
      user_cards.append(deal_card())
      computer_cards.append(deal_card())
    if calculate_score(user_cards) != 0 and calculate_score(computer_cards) != 0:
      while calculate_score(user_cards) < 21 and calculate_score(computer_cards) < 21:
        print("Your cards: {}, current score: {}".format(user_cards, sum(user_cards)))
        print("Computer's first card: {}".format(computer_cards[0]))
        choice2 = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if choice2 == "y":
          user_cards.append(deal_card())
          if calculate_score(computer_cards) < 17:
            computer_cards.append(deal_card())
          if calculate_score(user_cards) > 21 or calculate_score(computer_cards) > 21:
            break
        else:
          break

    print("Your final hand: {}, final score: {}".format(user_cards, sum(user_cards)))
    print("Computer's final hand: {}, final score: {}".format(computer_cards, sum(computer_cards)))
    if calculate_score(computer_cards) == 0:
      print("Opponent got a Blackjack! You lose.")
    elif calculate_score(user_cards) == 0:
      print("You got a Blackjack! You win.")
    elif calculate_score(user_cards) < calculate_score(computer_cards):
      print("The opponent's score is greater than yours. You lose.")
    elif calculate_score(user_cards) > 21:
      print("Your score is over 21. You decisively lose.")
    elif calculate_score(user_cards) > calculate_score(computer_cards):
      print("Your score is greater than the opponent's. You win.")
    elif calculate_score(computer_cards) > 21:
      print("The opponent's score is over 21. You decisively win.")
    elif calculate_score(user_cards) == calculate_score(computer_cards):
      print("It's a draw. No one wins.")
    choice3 = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ").lower()
    if choice3 == "n":
      flag = False
    else:
      clear()
