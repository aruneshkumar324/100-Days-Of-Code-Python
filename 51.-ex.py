# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

print(student_heights)
total_height = 0
len = 0
for height in student_heights:
  total_height += height
  len += 1

# print(total_height)
# print(len)

ave_height = total_height / len
print(round(ave_height))

# TEST
'''
a = 0

for x in range(1, 5):
  a += x
  print(x)
print(a)

for y in range(1, 10, 2):
  print(y)

'''