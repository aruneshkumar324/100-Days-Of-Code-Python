from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"


# -----------------------------     UI      --------------------------------
window = Tk()
window.title('Flashy')
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = PhotoImage(file='images/card_front.png')
canvas.create_image(400, 263, image=card_image)
canvas.create_text(400, 150, text='Title', font=('Arial', 40, 'italic'))
canvas.create_text(400, 250, text='Word', font=('Arial', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)


wrong_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(column=0, row=1)


right_image = PhotoImage(file='images/right.png')
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(column=1, row=1)
































window.mainloop()
