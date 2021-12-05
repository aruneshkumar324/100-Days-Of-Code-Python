# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# HIGHEST VALUE
highest = 0
for val in student_scores:
  if highest < val:
    highest = val

print(f"The highest score in the class is: {highest}")


# LOWEST VALUE FIND
lowest = 500

for val in student_scores:
  if lowest > val:
    lowest = val

print(f"The lowest score in the class is: {lowest}")
