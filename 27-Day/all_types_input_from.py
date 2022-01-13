

# https://replit.com/@arunesh1999/tkinter-widget-demo#main.py

from tkinter import *


window = Tk()
window.title('Widget Examples')
window.minsize(width=500, height=500)


# LABELS
label = Label(text='Old Text', font=('Arial', 12, 'bold'))
label.config(text='New Label Text')
label.pack()


# BUTTON
def clickMe():
    print('Hello Arunesh')
button = Button(text='Click Me', command=clickMe)
button.pack()


# ENTRY
entry = Entry(width=20)
entry.insert(END, string='Username')
print(entry.get())
entry.pack()


# TEXT
text = Text(width=20, height=5)
text.insert(END, 'You can write long character string here...')
print(text.get('1.0', END))
text.pack()


# SPINBOX
def spinbox_fun():
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, command=spinbox_fun)
spinbox.pack()


# SCALE
def scale_fun(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_fun)
scale.pack()


# CHECKBOX
def checkbutton_fun():
    print(checked_state.get())
checked_state = IntVar()
checkbutton = Checkbutton(text='Agree with policy ?', variable=checked_state, command=checkbutton_fun)
checked_state.get()
checkbutton.pack()


# RADIO BUTTON
def radio_fun():
    print(radio_state.get())

radio_state = IntVar()

radiobutton_male = Radiobutton(text='Male', value=1, variable=radio_state, command=radio_fun)
radiobutton_female = Radiobutton(text='Female', value=2, variable=radio_state, command=radio_fun)

radiobutton_male.pack()
radiobutton_female.pack()


#   LIST BOX
def listbox_fun(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
names = ['Mohan', 'Rohan', 'Sohan', 'Pohan']
for nm in names:
    listbox.insert(names.index(nm), nm)

listbox.bind('<<ListboxSelect>>', listbox_fun)
listbox.pack()



















window.mainloop()
