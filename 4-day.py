import my_module

import random

# 40 video
'''
random_integer = random.randint(1,10)
print(random_integer)

random_float = random.random() * 5
print(random_float)

# love score
love_score = random.randint(1,100)
print(f"Your love score is : {love_score}")


# print(my_module.firstName)
# print(my_module.lastName)
'''

# 42 VIDEO  - LIST
'''
letters = ['a','b','c','d','e','f','g','h','i']

print(letters)

print(letters[0])
print(letters[1])

print(letters[-1])
print(letters[-2])

letters[0] = "First"
print(letters[0])

items = ["Mohan","Sohan","Ram"]
print(items)

items.append("Pohan")
print(items)

items.extend(["Ram","Shyam","Sita"])
print(items)

items.sort()
print(items)

print(items.count("Ram"))
print(items.index("Sita"))

items.insert(5,"Hello")
print(items)

items.pop(5)
print(items)

items.pop()
print(items)

items.remove("Ram")
print(items)

items.reverse()
print(items)
'''

# 44 VIDEO  - Nested List
list = [1,2,3,4,5,6,7,8,9,10]
print(list)
print(len(list))
print(list[10 - 1])

dirty_food = ["Strawberries","Spinach","Kale","Nectarines","Apples","Grapes","Peaches","Cherries","Pears","Tomatoes"]

dirty_food.append("Test")

print(dirty_food)

good_food = ["Avocados","Sweet corn","Pineapples","Cabbages","Onions","Sweet peas","Papayas","Asparagus","Mangoes","Eggplants"]

final_list = [dirty_food, good_food]

print(final_list)

print(final_list[1][-1])