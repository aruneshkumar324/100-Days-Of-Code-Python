print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# 28 VIDEO - Control Flow, If/else statements
"""
if height > 120 :
  print("You can ride rollercoaster")
else:
  print("You are not eligible to ride rollercoaster")
"""
# comparision operator

# 30 VIDEO - Nested if statement and elif statement
"""
if height > 120 :
  print("You can ride rollercoaster")
  age = int(input("Enter your age? "))
  if age < 12:
    print("Please pay $5.")
  elif age <= 18:
    print("Please pay %7.")
  else:
    print("Please pay $12.")
else:
  print("You are not eligible to ride rollercoaster")
"""

# 33 VIDEO - Multiple if/else statements
"""
bill = 0

if height > 120 :
  print("You can ride rollercoaster")
  age = int(input("Enter your age? "))
  if age < 12:
    bill = 5
    print("Please pay $5.")
  elif age <= 18:
    bill = 7
    print("Please pay %7.")
  else:
    bill = 12
    print("Please pay $12.")

  photo = input("Do you want a photo taken? Y or N.")
  if photo == "y":
    bill += 5
  print(f"Total bil is : {bill}") 

else:
  print("You are not eligible to ride rollercoaster")
"""

# 35 VIDEO - Logical Operator
#   and,  or, not

bill = 0

if height > 120:
    print("You can ride rollercoaster")
    age = int(input("Enter your age? "))
    if age < 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay %7.")
    elif age >= 45 and age <= 55:
        print("Please pay $0.")
    else:
        bill = 12
        print("Please pay $12.")

    photo = input("Do you want a photo taken? Y or N.")
    if photo == "y":
        bill += 3
    print(f"Total bill is : {bill}")

else:
    print("You are not eligible to ride rollercoaster")