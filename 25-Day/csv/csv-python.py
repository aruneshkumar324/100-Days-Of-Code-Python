import csv

with open('people.csv', mode='r') as file_data:
    f = csv.reader(file_data)
    print(f)
