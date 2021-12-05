programming_dictionary = {
    "Bug":
    "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

# print(programming_dictionary)

# print(programming_dictionary["Function"])

# add item in dictionary
programming_dictionary["Loop"] = "This is loop in python"
# print(programming_dictionary)

programming_dictionary["Function"] = "New function message"
print(programming_dictionary["Function"])

# create empty dictionary

empty_dictionary = {}
empty_dictionary["First"] = "First dictionary item"
print(empty_dictionary)

empty_dictionary = {}
print(empty_dictionary)

for key in programming_dictionary:
    print(f"{key} -> {programming_dictionary[key]}")

print(len(programming_dictionary))

for key, value in programming_dictionary.items():
    print(f"{key} = {value}")

print()
print("--------------------------------------")
print()

first_dic = {
    "friends_name": ["Mohan", "Sohan", "Dohan", "Pohan"],
    "home": ["Bangalore", "Delhi", "Patna", "Mumbai"]
}

print(first_dic)

travel = {
    "City ": {
        "cities_visited": ["mathura", "Varindavan", "Agra"]
    },
    "state": {
        "state_visited": ["Delhi", "UP", "Uttrakhand"],
        "total_visited": 3
    }
}
print(travel)

second = [{
    "City ": {
        "cities_visited": ["mathura", "Varindavan", "Agra"]
    }
}, {
    "state": {
        "state_visited": ["Delhi", "UP", "Uttrakhand"],
        "total_visited": 3
    }
}]
