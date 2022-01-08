num = [1, 2, 3]

# # 1 METHOD
# new_numbers = []
# for n in num:
#     add = n + 1
#     new_numbers.append(add)
# print(new_numbers)


# 2 METHOD  ( list compression )

new_numbers = [n+2 for n in num]
print(new_numbers)


name = "Arunesh"
new_letters = [letter for letter in name]
print(new_letters)


new_list = [n*2 for n in range(1, 5)]
print(new_list)


names = ['Arunesh', 'Raj', 'Rohan', 'Ram', 'Salman', 'Neha']

short_names = [name for name in names if len(name) < 5]
print(short_names)

five_char_name = [name.upper() for name in names if len(name) > 5]
print(five_char_name)
























