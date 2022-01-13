from tkinter import *


window = Tk()
window.title("Counter GUI App")
window.minsize(width=300, height=150)

num = 0

label = Label(text=num, font=('Arial', 18, 'bold'))
label.pack()


def add(num):
    num += 1
    label.config(text=num)

button = Button(text='+', command=add)
button.pack()


window.mainloop()
