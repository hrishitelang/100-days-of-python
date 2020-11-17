#Write your code below this line 👇
def prime_checker(number):
  flag=0;
  for i in range(2, number):
    if number%i == 0:
      flag = 1
      break
  if number == 0 or number == 1:
    print("It is neither prime nor composite")
  elif number == 2:
    print("2 is the only even prime number")
  else:
    if flag == 0 and number != 1:
      print("It's a prime number.")
    else:
      print("It's not a prime number.")

#Write your code above this line 👆

#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
