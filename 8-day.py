# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

'''
def greet():
    print("Hello Arunesh")
    print("why you are not attending classes ?")
greet()
'''

'''
def greet(name):
    print(f"Hello {name}")
    print(f"{name}, why you are not attending classes ?")

greet('Arunesh')
'''

def greet(name, location):
    print(f"Hello {name}")
    print(f"You are from {location}")

# greet('Arunesh', 'Bangalore')
greet(location = "Delhi", name = "Ram")

print("-----------------------------")

def num(a,b,c):
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}")
num(5, 10, 15)

print("-----------------------------")

num(b=10, c=15, a=5)

print("-----------------------------")

def first(a=0,b=0,c=0):
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"c = {c}")

first(a=10, c=20)