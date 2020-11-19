#Calculator
from art import logo
#Addition
def add(a, b):
  return a+b

#Subtraction
def subtract(a, b):
  return a-b

#Multiplication
def multiply(a, b):
  return a*b

#Division
def divide(a, b):
  return a/b

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}



def calculator():
  print(logo)
  num1 = float(input("What is the first number? "))
  for k in operations:
    print (k)
  flag = True
  while flag:
    operator = input("Select the operator: ")
    num2 = float(input("What is the next number? "))
    for i in operations:
      if i == operator:
        answer = operations[i](num1, num2)
    print(f"{num1} {operator} {num2} = {answer}")
    choice=input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.:")
    if choice == 'n':
      flag = False
      calculator()
    elif choice == 'y':
      num1 = answer

calculator()
