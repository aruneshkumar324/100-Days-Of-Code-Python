# file = open('text.txt')
# content = file.read()
# print(content)
# file.close()


with open('text.txt') as file:
    content = file.read()
    print(content)

# with open("text.txt", mode='w') as file:
with open("text.txt", mode='a') as file:
    file.write("\nNew text wrote in file")

with open('new_file1.text', mode='a') as file:
    file.write("Hello Arunesh")


# with open("./../../../data.txt", mode='r') as file:
# with open("A:/data.txt", mode='r') as file:
    print(file.read())
