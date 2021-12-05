from random import randint

from art import logo, vs
from data import data

# RANDOM NUMBER GENERATE
def rand_num():
    return randint(0, 49)

# RANDOM GENERATE NUMBER STORE IN VARIBALE
first_rand_num = rand_num()
second_rand_num = rand_num()

score = 0
start = True

while start:
    print(logo)
    print(f"A : {data[first_rand_num]['follower_count']}")
    print(f"B : {data[second_rand_num]['follower_count']}")

    print(f"Compare A: {data[first_rand_num]['name']}, a {data[first_rand_num]['description']}, from {data[first_rand_num]['country']}.")
    print(vs)
    print(f"Against B: {data[second_rand_num]['name']}, a {data[second_rand_num]['description']}, from {data[second_rand_num]['country']}.")

    # ASK USER FOR COMPARE
    user_guess = input("Who has more followers? Type 'A' or 'B':  ").lower()

    if user_guess == "a":
        if data[first_rand_num]['follower_count'] > data[second_rand_num]['follower_count']:
            score += 1
            print(f"You're right! Current Score: {score}")
            first_rand_num = second_rand_num  
            second_rand_num = rand_num()  
        else:
            print(f"Sorry, that's wrong. Final Score: {score}")
            start = False
    elif user_guess == "b":
        if data[first_rand_num]['follower_count'] < data[second_rand_num]['follower_count']:
            score += 1
            print(f"You're right! Current Score: {score}")
            first_rand_num = second_rand_num  
            second_rand_num = rand_num()  
        else:
            print(f"Sorry, that's wrong. Final Score: {score}")
            start = False
    else:
        print("Invalid Input")
        start = False