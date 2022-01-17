from tkinter import *
import pandas
from random import randint, choice


BACKGROUND_COLOR = "#B1DDC6"


# -----------------------------     READ DATA FROM FILE      --------------------------------

# #  MY SOLUTION
# def generate_word():
#     data = pandas.read_csv('data/french_words.csv')
#     french = pandas.DataFrame(data)
#     french_word = french['French'][randint(0, 100)]
#     print(french_word)
#     canvas.itemconfig(update_text, text=french_word)

data = pandas.read_csv('data/french_words.csv')
print(data)

# to_learn = data.to_dict()
to_learn = data.to_dict(orient='records')
print(to_learn)


def next_card():
    current_card = choice(to_learn)
    print(current_card)
    canvas.itemconfig(update_title, text='French')
    canvas.itemconfig(update_word, text=current_card['French'])


# -----------------------------     UI      --------------------------------
window = Tk()
window.title('Flashy')
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = PhotoImage(file='images/card_front.png')
canvas.create_image(400, 263, image=card_image)
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
