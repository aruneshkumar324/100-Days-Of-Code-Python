# Write your code below this line 👇

def prime_checker(number):
    is_prime = True
    for x in range(2, number):
        if number % x == 0:
            is_prime = False

    if is_prime:
        print(f"{number} is Prime")
    else:
        print(f"{number} is not Prime")


# Write your code above this line 👆

# Do NOT change any of the code below👇
# n = int(Input("Check this number: "))
# prime_checker(number=n)

# PRINT 1 TO 50 PRIME NUMBER

num = 10

for x in range(2, num):
    if num % x == 0:
        print(f"{x} = Not Prime")
    else:
        print(f"{x} = Prime")

'''
PRINT 1 TO 100 NUMBER WITH PRIME OR NOT PRIME

1 IS PRIME
2 IS PRIME
.
.
.
100 IS PRIME

'''