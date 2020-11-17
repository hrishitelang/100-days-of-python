from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', /
'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', /
'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', /
'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift_amount, direction):
  if direction == "decode":
    shift_amount = shift_amount * -1
  text = [i for i in text]
  encrypt = []
  for char in text:
    if char in alphabet:
      a = alphabet.index(char)
      encrypt.append(alphabet[(a+shift_amount)%len(alphabet)])
    else:
      encrypt.append(char)
    text = "".join(encrypt)
  print(f"The {direction}d text is {text}")

print(logo)

flag = 1
while flag == 1:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text = text, shift_amount = shift, direction = direction)
  choice = input("Do you want to restart the cipher? Type 'yes' or 'no': ").lower()
  if choice == 'no':
      flag = 0
