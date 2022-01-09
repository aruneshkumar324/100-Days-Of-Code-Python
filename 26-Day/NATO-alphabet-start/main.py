import pandas as pd


data = pd.read_csv('nato_phonetic_alphabet.csv')


nato_data = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_data)


user = input("Enter a word: ").upper()
output = [nato_data[value] for value in user]
print(output)

