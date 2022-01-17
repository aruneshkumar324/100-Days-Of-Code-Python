from random import choice, randint, shuffle


# TODO  - compare unique id with in json data file
old_data = ['sXyUDaH65G', 'sXyUDfH65G', 'sXyUDae65G', 'sXyUkaH65G']

small_letters = list('abcdefghijklmnopqrstuvwxyz')
cap_letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
numbers = list('0123456789')

all_list_data = small_letters + cap_letters + numbers

unique_id = ''

def generate_unique_id(words):
    global unique_id
    shuffle(words)

    for x in range(0, 10):
        unique_id += all_list_data[x]

    if unique_id in old_data:
        generate_unique_id(all_list_data)
    else:
        print(unique_id)


generate_unique_id(all_list_data)
