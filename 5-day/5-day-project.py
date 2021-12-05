#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# EASY PASSWORD
password = ''
for let in range(0, nr_letters):
  password += random.choice(letters)
for sym in range(0, nr_symbols):
  password += random.choice(symbols)
for num in range(0, nr_numbers):
  password += random.choice(numbers)

print(password)

# HARD PASSWORD

password = []
for let in range(0, nr_letters):
  password.append(random.choice(letters))
for sym in range(0, nr_symbols):
  password += random.choice(symbols)
for num in range(0, nr_numbers):
  password += random.choice(numbers)

print(password)
random.shuffle(password)
print(password)

final_password = ''
for x in password:
  final_password += x
print(final_password)


'''
      ----------- MY SOLUTION  -----------


# RANDOM LETTER GENERATOR
rand_letter = ''
for let in range(0, nr_letters):
  rand_num = random.randint(0, len(letters) - 1)
  print(letters[rand_num])
  rand_letter += letters[rand_num]
print(rand_letter)

# RANDOM SYMBOLS
rand_symbols = ''
for sym in range(0, nr_symbols):
  rand_num = random.randint(0, len(symbols)-1)
  print(rand_num)
  rand_symbols += symbols[rand_num]
print(rand_symbols)

# RANDOM NUMBER GENERATOR
rand_number = ''
for num in range(0, nr_numbers):
  rand_num = random.randint(0, len(numbers)-1)
  print(rand_num)
  rand_number += numbers[rand_num]
print(rand_number)

# FINAL RANDOM PASSWORD
easy_method = rand_letter + rand_symbols + rand_number
print(easy_method)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

easy_password = rand_letter + rand_symbols + rand_number
list_password = list(easy_password)
print(list_password)
print(len(list_password))

hard_pass = ''
for x in range(0, len(easy_password)):
  rand_num = random.randint(0, len(list_password)-1)
  hard_pass += list_password[rand_num]
print(hard_pass)

'''