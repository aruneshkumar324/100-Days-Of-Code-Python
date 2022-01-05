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

# print(type(data))
# print(type(data['temp']))

# data_dict = data.to_dict()
# print(data_dict)
#
#
# data_json = data.to_json()
# print(data_json)
#
# data_list = data['temp'].to_list()
# print(data_list)

# data_list_1 = data['day'].to_list()
# print(data_list_1)

# for day in data_list_1:
#     print(day)


# ##  1 - METHOD
# aveg_temp = 0
# total_temp = 0
#
# for tem in data_list:
#     aveg_temp += tem
#     total_temp += 1
#
# print(aveg_temp / total_temp)


# # 2 - METHOD
# avegrag_temp = sum(data_list) / len(data_list)
# print(avegrag_temp)


# ##  3 - METHOD
# aveg_temp = data['temp'].mean()
# print(aveg_temp)
#
#
# print(data['temp'].count())
#
# print(data['temp'].median())
#
# print(data['temp'].min())
# print(data['temp'].max())
# print(data['temp'].unique())


## GET COLUMN
get_col = data['condition']
print(get_col)
print(data.condition)


## GET ROW

get_row = data[data.day == 'Thursday']
print(get_row)

get_row_a = data[data['day'] == 'Thursday']
print(get_row_a)


get_high_temp = data[data.temp == data['temp'].max()]
print(get_high_temp)

#
# high_temp = data['temp'].max()
# print(high_temp)




















