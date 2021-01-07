with open('file1.txt') as file1, open('file2.txt') as file2:
  x = file1.readlines()
  x = [int(i.rstrip()) for i in x]
  y = file2.readlines()
  y = [int(i.rstrip()) for i in y]
  result = [i for i in x if i in y]

# Write your code above 👆

print(result)
