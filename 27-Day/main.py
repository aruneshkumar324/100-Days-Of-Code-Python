import tkinter


window = tkinter.Tk()


window.title("My First GUI App")
window.minsize(width=500, height=300)

# components
label = tkinter.Label(text="Label Test", font=("Arial", 18, "bold"))
# label.pack()
# label.pack(side='top')  # right, bottom, left, top
label.pack(expand=True)


# WINDOW SCREEN SHOW
window.mainloop()
