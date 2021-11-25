#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

import random

rand = random.randint(0,1)
# rand = random.randint("Heads","Tails")

print(rand)

if rand == 0:
  print("Heads")
else:
  print("Tails")