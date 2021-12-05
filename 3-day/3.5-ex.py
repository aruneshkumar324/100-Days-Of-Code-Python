# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇

final_name = name1+" "+name2

final_name = final_name.lower()

t = final_name.count("t")
r = final_name.count("r")
u = final_name.count("u")
e = final_name.count("e")

l = final_name.count("l")
o = final_name.count("o")
v = final_name.count("v")
e = final_name.count("e")

true = str(t+r+u+e)
love = str(l+o+v+e)

score = true + love

score = int(score)

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")