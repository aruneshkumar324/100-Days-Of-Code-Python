#Write your code below this row 👇

'''
You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:
'''
total = 0
for num in range(2, 101, 2):
  total += num
print(total)

# MY SOLUTION
num = 0
for even in range(1, 101):
  if even  % 2 == 0:
    num += even
print(num)