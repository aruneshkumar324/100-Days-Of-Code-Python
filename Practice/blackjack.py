import random

import blackjackart

def blackjack():

    # ask for play again
    def play_again():
        ask = input("Do you want to pplay a game of Black? Type 'y' or 'n': ")
        if ask == "y":
            blackjack()

    # logo
    print(blackjackart.logo)

    # all card in list
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    # random card generator
    def randCard(cards):
        return random.choice(cards)

    user = [randCard(cards), randCard(cards)]
    dealer = [randCard(cards), randCard(cards)]

    # calculate total card number
    total_user = 0
    for x in user:
        total_user += x

    total_dealer = 0
    for x in dealer:
        total_dealer += x

    print(f"Your cards: {user}, current score : {total_user}")
    print(f"Computer's first card: {dealer[0]}")

    # ask user do you want generate again new card
    get_another_card = total_user <= 21
    while get_another_card:
        new_card = input("Type 'y' to get another card, type 'n' to pass: ")

        if new_card == "y":
            total_user = 0
            user.append(randCard(cards))
            for x in user:
                total_user += x
            print(f"Your cards: {user}, current score : {total_user}")
            if total_user > 21:
                get_another_card = False
        elif new_card == "n":
            get_another_card = False

    if total_dealer < 21:
        total_dealer = 0
        dealer.append(randCard(cards))
        for x in dealer:
            total_dealer += x
        print("testing")
        print(dealer)
        print(total_dealer)


    # check winner -> using of user & dealer value
    if total_user == total_dealer:
        print("Draw")
        play_again()
    elif total_user < 22 :
        if total_user > total_dealer:
            print("Opponent went over. You win 😁")
            play_again()
    elif  total_dealer < 22:
        if total_dealer > total_user:
            print("You went over. You lose 😢")
            play_again()
    else:
        print("You went over. You lose 😢")

# call game function if user want play game
game_start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

if game_start == "y":
    blackjack()
