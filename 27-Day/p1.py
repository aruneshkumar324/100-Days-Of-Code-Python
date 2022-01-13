from tkinter import *


window = Tk()
window.title("1 Practice GUI")
window.minsize(width=500, height=250)

label = Label(text='Hello Arunesh', font=('Arial', 18, 'bold'))
label.pack()


input = Entry(width=20)
input.pack()


def btn():
    print('Hello Arunesh')
    input_content = input.get()
    label.config(text=input_content)


button = Button(text='Click Me', command=btn)
button.pack()


window.mainloop()
