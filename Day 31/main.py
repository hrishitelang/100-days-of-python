BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas as pd
import random

#---------------------------- UI DESIGN ----------------------------#


def change_word():
    global french_word
    canvas.delete(french_word)
    french_word = canvas.create_text(400, 263, text=data['French'].iloc[random.randint(0, 100)], font=('Arial', 40, "bold"))


#---------------------------- UI DESIGN ----------------------------#


window = Tk()
window.config(width=1000, height=1000, padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title('Flashy')
canvas = Canvas(width=800, height=525, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=1, column=1, columnspan=2)

card_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_image)
canvas.create_text(400, 100, text='French', font=('Arial', 40, "italic"))

data = pd.read_csv('data/french_words.csv')
word = data['French'].iloc[random.randint(0, 100)]
french_word = canvas.create_text(400, 263, text=word, font=('Arial', 40, "bold"))

# language = Label(text="Title", justify=CENTER,font=('Arial', 40, "italic"), bg='white')
# language.place(x=340, y=100)

# french_word = Label(text='word', justify=CENTER, font=('Arial', 60, "bold"), bg='white')
# french_word.place(x=300, y=263)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=change_word)
wrong_button.grid(row=2, column=1)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=change_word)
right_button.grid(row=2, column=2)

window.mainloop()
