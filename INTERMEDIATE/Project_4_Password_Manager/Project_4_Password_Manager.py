from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

#labels
website_label = Label(text="Website")
website_label.grid(row=1)
email_label = Label(text="Email")
email_label.grid(row=2)
password_label = Label(text="Password")
password_label.grid(row=3)



window.mainloop()
