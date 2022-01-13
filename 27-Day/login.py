from tkinter import *

window = Tk()
window.title('Login Form')
window.minsize(width=750, height=500)


label = Label(text='Login Form', font=('Arial', 15, 'bold'))
label.pack()


username = Entry()
username.pack()


password = Entry()
password.pack()









window.mainloop()
