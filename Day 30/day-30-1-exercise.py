fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
  try:
    fruit = fruits[index]
  except IndexError as error::
    print(f"The error '{error}' means that the index is out of bounds.")
    print("Fruit Pie")

  else:
    print(fruit + " pie")

try:
  make_pie(4)
