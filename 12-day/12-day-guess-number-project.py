import random

print("""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.""")

guess = random.randint(1, 100)
print(f"Passt, the correct answer is 63")  # testing purpose

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")


def compare(attempts_number):
    attempts_loop = True
    attempts = attempts_number

    while attempts_loop:
        user_guess = int(input("Make a guess: "))

        if attempts == 0 and user_guess != guess:
            print("You've run out of guesses, you lose.")
            attempts_loop = False

        elif user_guess == guess:
            print(f"You got it! The answer was {guess}")
            attempts_loop = False

        elif user_guess > guess:
            print("To High")
            print("Guess again.")
            attempts -= 1
            print(f"You have {attempts + 1} attempts remaning to guess the number.")
        elif user_guess < guess:
            print("To Low")
            print("Guess again.")
            attempts -= 1
            print(f"You have {attempts + 1} attempts remaning to guess the number.")


if difficulty == 'easy':
    print("You have 10 attempts remaning to guess the number.")
    compare(9)
elif difficulty == 'hard':
    print("You have 5 attempts remaning to guess the number.")
    compare(4)

'''             ANGELA SOLUTION

from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = Input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(Input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")

game()

'''