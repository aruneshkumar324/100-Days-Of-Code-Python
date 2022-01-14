from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas_photo = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=canvas_photo)
canvas.create_text(100, 130, text='00:00', font=(FONT_NAME, 15, 'bold'), fill='white')
canvas.grid(column=1, row=1)


timer_label = Label(text='Timer', font=(FONT_NAME, 50, 'bold'), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)


start_button = Button(text='Start', highlightthickness=0)
start_button.grid(column=0, row=2)


reset_button = Button(text='Reset')
reset_button.grid(column=2, row=2)


check_label = Label(text='✔', font=(FONT_NAME, 12, 'bold'), fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)










window.mainloop()
