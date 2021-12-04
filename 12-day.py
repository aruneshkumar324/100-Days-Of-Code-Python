################### Scope ####################

enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


def game_status():
    def game():
        game_start = True
        print(game_start)
    game()

# print(game_start)
game_status()

# 117 VIDEO
friends = ['Mohan','Sohan','Dohan']

# def friend():
#     if 5 > 2:
#         b_friend = friends[0]
# print(b_friend)

if 5 > 2:
    best_friend = friends[0]
print(best_friend)

for x in friends:
    fri = x

print(fri) # last value will print

# 118 VIDEO

sum = 5

def cal():
    # global sum # don't use it'll create BUG
    print(f"Local Sum = {sum}")
    return sum + 10

cal()

print(f"Global Sum = {sum}")

# 199 - VIDEO   (constant variable)

PI = 3.1434
URL = "https://www.google.com/"
print(PI)
