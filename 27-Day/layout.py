from tkinter import *

window = Tk()
window.title("My First GUI App")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

label = Label(text="Label Test", font=("Arial", 18, "bold"))
# label.pack()
# label.place(x=50, y=10)
label.grid(column=0, row=0)
label.config(padx=50, pady=50)


def button_clicked():
    print("Clicked Me Someone")
    label.config(text=input.get())
button = Button(text='Click Me', command=button_clicked)
# button.pack()
button.grid(column=1, row=1)


input = Entry(width=20)
# input.pack()
input.grid(column=3, row=2)


# NEW BUTTON
new_button = Button(text='New Button')
new_button.grid(column=2, row=0)



















window.mainloop()
