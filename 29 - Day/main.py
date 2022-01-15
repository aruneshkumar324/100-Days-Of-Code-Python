from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)

    print(f"Your password is: {password}")

    password_entry.insert(0, password)

    # https://pypi.org/project/pyperclip/
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()

    # messagebox.showinfo(title='Title', message='Hello Arunesh')

    # if website == "" or password == "":
    if len(website.strip()) == 0 or len(password.strip()) == 0:
        messagebox.showinfo(title='Oops', message="Please don't leave any fields empty!")
    else:
        it_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email_username} \nPassword: {password} \n")

        if it_ok:
            with open('data.txt', 'a') as dataFile:
                dataFile.write(f'{website} | {email_username} | {password}\n')

                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)


# IMAGE DESIGN
canvas = Canvas(width=200, height=200)
logo_photo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_photo)
canvas.grid(column=1, row=0)


# WEBSITE
website_label = Label(text='Website')
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky='EW')


# EMAIL OR USERNAME
email_username_label = Label(text='Email/Username')
email_username_label.grid(column=0, row=2)

email_username_entry = Entry(width=35)
email_username_entry.insert(0, 'example.@gmail.com')
email_username_entry.grid(column=1, row=2, columnspan=2, sticky='EW')


# PASSWORD
password_label = Label(text='Password')
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky='EW')

generate_password_button = Button(text='Generate Password', command=generate_password)
generate_password_button.grid(column=2, row=3, sticky='EW')


# ADD PASSWORD
add_button = Button(text='Add', width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky='EW')
































window.mainloop()
