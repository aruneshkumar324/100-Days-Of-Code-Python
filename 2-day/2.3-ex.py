# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


remainingAge = 90 - int(age)

days = 365 * remainingAge
weeks = 52 * remainingAge
months = 12 * remainingAge

print(remainingAge)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")

