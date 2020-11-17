alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
def caesar(text, shift_amount, direction):
  if direction == "decode":
    shift_amount = shift_amount * -1
  text = [i for i in text]
  encrypt = []
  for letter in text:
    a = alphabet.index(letter)
    encrypt.append(alphabet[(a+shift_amount)%len(alphabet)])
    text = "".join(encrypt)
  print(f"The {direction}d text is {text}")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(text = text, shift_amount = shift, direction = direction)
