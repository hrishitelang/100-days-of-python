from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program.")
flag = True
auction = {}
while flag:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  auction[name] = bid
  choice = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
  if choice == "no":
    flag = False
  elif choice == "yes":
    clear()

def winner(auction):
  winner = ''
  max = 0
  for k in auction:
    if auction[k] > max:
      winner = k
      max = auction[k]
  #winner = max(auction, key=auction.get)
  print(f"The winner is {winner} with a bid of ${max}")

winner(auction)
