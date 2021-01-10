from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_text():
    name_answer = name_text.get()
    email_answer = email_text.get()
    password_answer = password_text.get()

    if name_answer == "":
        messagebox.showerror(title="Error", message="Please enter the name of the website.")
        if email_answer == "":
            messagebox.showerror(title="Error", message="Please enter your email address.")

        if password_answer == "":
            messagebox.showerror(title="Error", message="Please enter your password.")
    else:
        flag = messagebox.askokcancel(title=name_answer, message=f"Here are the details:\nSite: {name_answer}\nEmail: {email_answer}\nPassword: {password_answer}\n"
                                                                 f"Are you sure you want to save these details?")

        if flag:
            with open('data.txt', 'a') as file:
                file.write(f"{name_answer} | {email_answer} | {password_answer}\n")
            name_text.delete(0, 'end')
            email_text.delete(0, 'end')
            password_text.delete(0, 'end')

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
name_text.focus()

email_label = Label(text="Email/Username:")
email_label.grid(row=3, column=1)

email_text = Entry(width=39)
email_text.grid(row=3, column=2, columnspan=2)
email_text.insert(0,"telang.hrishikesh@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=4, column=1)

password_text = Entry(width=21, textvariable=StringVar())
password_text.grid(row=4, column=2)

generate_password = Button(text="Generate Password")
generate_password.grid(row=4, column=3)

add = Button(text="Add", width=36, command=save_text)
add.grid(row=5, column=2, columnspan=2)


window.mainloop()