from tkinter import *
from tkinter import messagebox
import json
from random import shuffle, randint


# ---------------------------------------    GENERATE UNIQUE ID  -----------------------------------------
# TODO  - compare unique id with in json data file
old_data = ['sXyUDaH65G', 'sXyUDfH65G', 'sXyUDae65G', 'sXyUkaH65G']

small_letters = list('abcdefghijklmnopqrstuvwxyz')
cap_letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
numbers = list('0123456789')

all_list_data = small_letters + cap_letters + numbers


# ---------------------------------------    DATA SAVE METHOD  -----------------------------------------
def signup():
    # GENERATE UNIQUE ID
    unique_id = ''
    shuffle(all_list_data)
    for x in range(0, randint(10, 16)):
        unique_id += all_list_data[x]

    username_email = username_email_entry.get()
    name = name_entry.get()
    password = password_entry.get()

    signup_data = {
        username_email: {
            "id": unique_id,
            "Username OR Email": username_email,
            "Name": name,
            "Password": password,
        }
    }

    try:
        with open('db/account.json', 'r') as file_data:
            data = json.load(file_data)

        # print(data[][])

    except FileNotFoundError:
        with open('db/account.json', 'w') as file_data:
            json.dump(signup_data, file_data, indent=4)

    else:
        data.update(signup_data)

        with open('db/account.json', 'w') as file_data:
            json.dump(data, file_data, indent=4)

        messagebox.showinfo(title='Successfully', message=f'Welcome {name}')

    finally:
        unique_id = ''
        username_email_entry.delete(0, END)
        name_entry.delete(0, END)
        password_entry.delete(0, END)




# ---------------------------------------    UI  -----------------------------------------------

window = Tk()
window.title('Create New Account')
window.minsize(width=250, height=250)
window.config(pady=20, padx=20)


# LOGO ON CANVAS
canvas = Canvas(width=491, height=241)
signup_photo = PhotoImage(file='signup.png')
canvas.create_image(250, 60, image=signup_photo)
canvas.grid(column=1, row=0)


# LABELS AND INPUT FORMS

username_email_label = Label(text='Username/Email :')
username_email_label.grid(column=0, row=1)
username_email_label.config(padx=20, pady=5)

username_email_entry = Entry(width=30)
username_email_entry.grid(column=1, row=1, columnspan=2, sticky='EW')


name_label = Label(text='Full Name :')
name_label.grid(column=0, row=2)
name_label.config(pady=20, padx=5)

name_entry = Entry(width=30)
name_entry.grid(column=1, row=2, columnspan=2, sticky='EW')


password_label = Label(text='Password :')
password_label.grid(column=0, row=3)
password_label.config(padx=20, pady=5)

password_entry = Entry(width=20)
password_entry.grid(column=1, row=3, sticky='EW')


password_button = Button(text='Generate Password')
password_button.grid(column=2, row=3)

signup_button = Button(text='Sign Up', command=signup)
signup_button.grid(column=1, row=4)





























window.mainloop()
