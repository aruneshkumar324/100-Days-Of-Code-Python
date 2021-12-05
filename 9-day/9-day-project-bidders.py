from replit import clear
# HINT: You can call clear() to clear the output in the console.

import biddersart

print(biddersart.logo)

bidders = {}

result = True

while result:
    name = input("What is your name ? : ")
    amount = int(input("What is your bid ? : $"))
    bidders_there = input("Are there any other bidders? Type 'yes' or 'no'. ")

    bidders[name] = amount

    if bidders_there == "yes":
        clear() # it'll not work here
    elif bidders_there == "no":
        result = False

        # compare bidders amount
        x = 0
        winner = ''
        for key in bidders:
            val = bidders[key]
            if val > x:
                x = val
                winner = key

        print(f"The winner is {winner} with a bid of {x}")

print(bidders)
