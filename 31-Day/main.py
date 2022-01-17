from tkinter import *
import pandas
from random import randint, choice

import time


BACKGROUND_COLOR = "#B1DDC6"

def demo():
    print('first')
    time.sleep(2)
    print('second')

# demo()


# -----------------------------     READ DATA FROM FILE      --------------------------------

data = pandas.read_csv('data/french_words.csv')
to_learn = data.to_dict(orient='records')

current_card = {}


def next_card():
    global current_card, timer_flip
    window.after_cancel(timer_flip)
    current_card = choice(to_learn)
    canvas.itemconfig(update_title, text='French', fill="black")
    canvas.itemconfig(update_word, text=current_card['French'], fill="black")
    canvas.itemconfig(canvas_image, image=front_image)
    timer_flip = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(update_title, text="English", fill="white")
    canvas.itemconfig(update_word, text=current_card['English'], fill="white")


# -----------------------------     UI      --------------------------------
window = Tk()
window.title('Flashy')
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

timer_flip = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file='images/card_front.png')
back_image = PhotoImage(file="images/card_back.png")

canvas_image = canvas.create_image(400, 263, image=front_image)
update_title = canvas.create_text(400, 150, text='French', font=('Arial', 40, 'italic'))
update_word = canvas.create_text(400, 250, text='word', font=('Arial', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)


wrong_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)


right_image = PhotoImage(file='images/right.png')
right_button = Button(image=right_image, highlightthickness=0, command=next_card)
right_button.grid(column=1, row=1)


next_card()



























window.mainloop()
