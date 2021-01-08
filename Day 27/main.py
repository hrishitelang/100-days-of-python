from tkinter import *

window = Tk()
window.title('My Tkinter Project')
window.minsize(width=600, height=400)
label = Label(text="This is my label", font=('Arial', 20,'bold'))
label.pack()

def click_button():
    label['text'] = textbox.get()


button = Button(text='Click me', command=click_button)
button.pack()
textbox = Entry()
textbox.pack()

window.mainloop()