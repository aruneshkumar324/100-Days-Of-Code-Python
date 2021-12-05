import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

rps = [rock, paper, scissors]

# user input for RPS
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))


# computer random RPS
print("Computer chose:")
randRPS = random.randint(0, 2)

# rule apply
if user >= 3 or user < 0:
  print("You typed an invalid number, you lose!")
else:
  print(rps[user])
  print(rps[randRPS])
  if rps[user] == rps[randRPS]:
    print("It's Draw")
  elif rps[user] == rps[0] and rps[randRPS] == rps[2]:
    print("You win!")
  elif rps[user] == rps[1] and rps[randRPS] == rps[0]:
    print("You win!")
  elif rps[user] == rps[2] and rps[randRPS] == rps[1]:
    print("You win!")
  else:
    print("You lose")