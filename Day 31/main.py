BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas as pd
import random

#---------------------------- UI DESIGN ----------------------------#



window = Tk()
window.config(width=1000, height=1000, padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title('Flashy')
canvas = Canvas(width=800, height=525, bg=BACKGROUND_COLOR, highlightthickness=0)

card_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_image)
canvas.grid(row=1, column=1, columnspan=2)

language = Label(text="Title", justify=CENTER,font=('Arial', 40, "italic"), bg='white')
language.place(x=340, y=100)

data = pd.read_csv('data/french_words.csv')
#word = data['French'].iloc[random.randint(0,100)]
french_word = Label(text='word', justify=CENTER, font=('Arial', 60, "bold"), bg='white')
french_word.place(x=300, y=263)

wrong_image = PhotoImage(file="images/wrong.png")
button1 = Button(image=wrong_image, highlightthickness=0)
button1.grid(row=2, column=1)

right_image = PhotoImage(file="images/right.png")
button2 = Button(image=right_image, highlightthickness=0)
button2.grid(row=2, column=2)

window.mainloop()
