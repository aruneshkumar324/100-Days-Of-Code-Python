# ##  MY SOLUTION
#
# list1 = []
# list2 = []
#
# with open('file1.txt') as file1:
#     for row in file1:
#         row = row.strip('\n')
#         list1.append(row)
#
# with open('file2.txt') as file2:
#     for row in file2:
#         row = row.strip('\n')
#         list2.append(row)
#
# result = [int(n) for n in list1 if n in list2]
#
# print(result)


# ANGELA SOLUTION
with open('file1.txt') as file1:
    file1_data = file1.readlines()

with open('file2.txt') as file2:
    file2_data = file2.readlines()

result = [int(n) for n in file1_data if n in file2_data]
print(result)
