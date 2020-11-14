# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

a = 0
#Write your code below this row 👇
for i in student_heights:
  a = a + i

average = round(a/len(student_heights))
print(average)
