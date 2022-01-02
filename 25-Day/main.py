# # 1 - METHOD
# with open('weather_data.csv', mode='r') as file:
#     for x in file:
#         x = x.strip('\n')
#         print(x)
#
# # 2 - METHOD
# with open('weather_data.csv', mode='r') as data:
#     print(data.read())

# #  3 - METHOD
# with open('weather_data.csv', mode='r') as file_data:
#     f = file_data.readlines()
#     print(f)

# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)


import pandas

data = pandas.read_csv('weather_data.csv')
print(data)

print()

print(data['temp'])


students = pandas.read_csv('4th-7A-year-students-details.csv')
print(students['NAME'])




















