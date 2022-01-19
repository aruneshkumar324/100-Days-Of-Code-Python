from tkinter import *
from tkinter import messagebox
import smtplib


#  ------------------------     VARIABLES      -----------------------------------------
my_email = "pythonemailtesting76@gmail.com"
password = "9534857622"

receiver_mail = "pythonemailtesting76@yahoo.com"


#  ------------------------     METHODS      -----------------------------------------
def send_mail():
    sender_mail = sender_mail_entry.get()
    sender_password = sender_mail_password_entry.get()
    r_mail = receiver_mail_entry.get()
    subject = subject_entry.get()
    message = message_mail_entry.get("1.0", "end-1c")

    print(sender_mail)
    print(sender_password)
    print(r_mail)
    print(subject)
    print(message)

    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=sender_mail, password=sender_password)
            connection.sendmail(from_addr=sender_mail, to_addrs=r_mail, msg=f"Subject:{subject}\n\n{message}")

        messagebox.showinfo(title="Successful", message="Mail Sent")

    except smtplib.SMTPAuthenticationError:
        messagebox.showinfo(title='Failed', message="Please check you input data.")

    finally:
        subject_entry.delete(0, END)
        message_mail_entry.delete("1.0", "end-1c")


#  ------------------------     UI      -----------------------------------------

window = Tk()
window.title("Mail Sender")
window.config(padx=20, pady=20)


# LOGO
canvas = Canvas(width=175, height=131)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(88, 66, image=logo_image)
canvas.grid(column=0, row=0, columnspan=2)


# FORMS
sender_mail_label = Label(text='Sender Mail :')
sender_mail_label.grid(column=0, row=1, pady=10)

sender_mail_entry = Entry(width=40)
sender_mail_entry.insert(0, my_email)
sender_mail_entry.grid(column=1, row=1)


sender_mail_password_label = Label(text='Password :')
sender_mail_password_label.grid(column=0, row=2, pady=10)

sender_mail_password_entry = Entry(width=40)
sender_mail_password_entry.insert(0, password)
sender_mail_password_entry.grid(column=1, row=2)


receiver_mail_label = Label(text='Receiver Mail :')
receiver_mail_label.grid(column=0, row=3, pady=10)

receiver_mail_entry = Entry(width=40)
receiver_mail_entry.insert(0, receiver_mail)
receiver_mail_entry.grid(column=1, row=3)


subject_mail_label = Label(text='Subject : ')
subject_mail_label.grid(column=0, row=4, pady=10)

subject_entry = Entry(width=40)
subject_entry.grid(column=1, row=4)


message_mail_label = Label(text="Message")
message_mail_label.grid(column=0, row=5, pady=10)

message_mail_entry = Text(window, width=30, height=5)
message_mail_entry.grid(column=1, row=5)


button = Button(text='Send Mail', command=send_mail)
button.grid(column=0, row=6, columnspan=2, pady=10)























window.mainloop()
