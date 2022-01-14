from tkinter import *


FONT = ('Arial', 12)


window = Tk()
window.title('Mile to Km Converter')
window.iconbitmap('icon.ico')
# window.minsize(width=300, height=200)
window.config(padx=20, pady=20)


entry = Entry(width=10)
entry.grid(column=1, row=0)


miles_label = Label(text='Miles', font=FONT)
miles_label.grid(column=2, row=0)
miles_label.config(padx=20, pady=20)


equal_label = Label(text='is equal to', font=FONT)
equal_label.grid(column=0, row=1)


result = 0
result_label = Label(text=result, font=FONT)
result_label.grid(column=1, row=1)
result_label.config(padx=10, pady=10)


km_label = Label(text='Km', font=FONT)
km_label.grid(column=2, row=1)


# CALCULATION OPERATION

def calculate():
    miles = float(entry.get())
    km = miles * 1.60934
    print(km)
    result_label.config(text=round(km, 2))

button = Button(text='Calculate', command=calculate)
button.grid(column=1, row=2)
























window.mainloop()
