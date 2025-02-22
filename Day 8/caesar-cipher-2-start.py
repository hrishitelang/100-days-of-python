alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
z = len(alphabet)

def encrypt(plain_text, shift_amount):
  plain_text = [i for i in text]
  encrypt = []
  for letter in plain_text:
    a = alphabet.index(letter)
    encrypt.append(alphabet[(a+shift_amount)%z])
  plain_text = "".join(encrypt)
  print(f"The encoded text is {plain_text}")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
  #e.g.
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"
def decrypt(cipher_text, shift_amount):
  cipher_text = [i for i in text]
  decrypt = []
  for letter in cipher_text:
    a = alphabet.index(letter)
    decrypt.append(alphabet[(a-shift_amount)%z])
  cipher_text = "".join(decrypt)
  print(f"The decoded text is {cipher_text}")

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == 'encode':
  encrypt(plain_text=text, shift_amount=shift)
if direction == 'decode':
  decrypt(cipher_text=text, shift_amount=shift)
