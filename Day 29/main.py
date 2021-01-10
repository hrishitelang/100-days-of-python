from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
# window.minsize(400,400)
window.config(padx=40, pady=40)

canvas = Canvas(height=200, width=200)
image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(row=1, column=2)

name_label = Label(text="Website:")
name_label.grid(row=2, column=1)

name_text = Entry(width=39)
name_text.grid(row=2, column=2, columnspan=2)

email_label = Label(text="Email/Username:")
email_label.grid(row=3, column=1)

email_text = Entry(width=39)
email_text.grid(row=3, column=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(row=4, column=1)

password_text = Entry(width=21)
password_text.grid(row=4, column=2)

generate_password = Button(text="Generate Password")
generate_password.grid(row=4, column=3)

add = Button(text="Add", width=36)
add.grid(row=5, column=2, columnspan=2)


window.mainloop()