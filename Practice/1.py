# FIRST EXAMPLE
class First:
    firstName = "Arunesh"


print(First)

a = First()
print(a.firstName)


#SECOND EXMAPLE
class Second:
    def __init__(self, name, age):
        self.name = name
        self.age = age


b = Second("Arunesh kumar", 22)
print(f"Hello {b.name}, you are {b.age} years old")


# THIRD EXAMPLE
class Third:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello {self.name}, you are {self.age} years old."

    def hello(self):
        print("Hello arunesh")


c = Third("Mohan", 35)

print(c.greet())
c.hello()

print()
print()


# FOURTH EXAMPLE
class Four:
    def __init__(xyz, name):
        xyz.name = name

    def greet(abc):
        print(f"Hello {abc.name}")

d = Four("Sohan")
d.greet()


# FIVE EXAMPLE
class Five:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print(f"hello {self.name}, your age is {self.age}")

e = Five("Ram", 64)
e.hello()

e.age = 50
e.hello()

print(e.name)
print(e.age)

# del e.age
# print(e.age)
#
# del e
# e.hello()



# SIX EXAMPLE

class Six:
    pass
















