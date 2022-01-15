from tkinter import *


window = Tk()
window.title("Counter GUI App")
window.minsize(width=300, height=150)

num = 0

label = Label(text=num, font=('Arial', 18, 'bold'))
label.pack()


def increase():
    global num
    num += 1
    label.config(text=num)

increase_button = Button(text='+', command=increase)
increase_button.pack()


def decrease():
    global num
    num -= 1
    label.config(text=num)

decrease_button = Button(text='-', command=decrease)
decrease_button.pack()

def reset():
    global num
    num = 0
    label.config(text=num)

reset_button = Button(text='Reset', command=reset)
reset_button.pack()



window.mainloop()
