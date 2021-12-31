"""
18 VIDEO - Data Types
"""

#STRING
print(len("Arunesh"))

# sub script
print("Arunesh"[0])
print("Arunesh"[-1])
print("Arunesh"[6])

print("1"+"2")

#NUMBER
print(1+2)
print(1_2_3)
print(1,2,3)

#FLOAT
print(1.2 + 2.1)
print(3/2)

#BOOLEAN
print(True)
print(False)

"""
19 VIDEO - type conversion
"""
print("----- 19 VIDEO -----")

print(type(5))
print(type("Arunesh"))
print(type(12.345))
print(type(True))

# print(len(123))
print(len(str(123)))

# print("Hello "+ 1)
print("Hello " + str(1))

print(70 + float("30.5"))

print(5+5)
print(str(5) + str(5))

print(str(5) + "Hello")
print("Hello "+ str(5))

# name = Input("Enter your name\n")
# name_count = len(name)
# print(type(name_count))
# print("Your name has "+ str(name_count) + " characters")



"""
21 VIDEO - type conversion
"""

# PEMDAS

# ()
# **
# * /
# + -

# 3*3+3/3-3

"""
23 VIDEO - Number Manipulation
"""
print()
print("----- 23 VIDEO - Number Manipulation -----")
print()

x = 8 / 3

print(x)
print(int(x))
print(round(x))
print(round(x, 2))

# floor division
print(8/3)
print(type(8/3))
print(8//3)
print(type(8//3))

score = 10
print(score)

# score += 5
# score -=5
# score *=5
score /= 5
print(score)

# F-STRING
firstName = "Arunesh"
age = 22
student = True

print("Hello "+firstName+", your age is "+str(age)+" and are you student ? "+str(student))

print(f"Hello {firstName}, your age is {age} and are you student ? {student}")