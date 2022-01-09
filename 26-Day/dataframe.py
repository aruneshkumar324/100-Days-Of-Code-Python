import pandas

student_data = {
    "names": ['Arunesh', 'Rohan', 'Mohan', 'Sohan', 'Dohan'],
    "score": [43, 61, 75, 85, 28]
}

# print(student_data)

# # 1 - METHOD
# for (key, value) in student_data.items():
#     print(key)
#     print(value)


# 2 - METHOD
student_data_frame = pandas.DataFrame(student_data)
print(student_data_frame)

# for (key, value) in student_data_frame.items():
#     print(value)

for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(key.names)
    print(row.score)


for (index, row) in student_data_frame.iterrows():
    # if row.names == 'Sohan':
    #     print(row.score)
    if row.score >= 50:
        print(row.names)

















