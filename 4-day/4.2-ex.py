import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


print(names)

nameLength = len(names)

randNumber = random.randint(0, nameLength - 1)

print(f"{names[randNumber]} is going to buy the meal today!")