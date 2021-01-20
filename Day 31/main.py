from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- FUNCTIONS TO DESCRIBE ---------------------------- #
data = pd.read_csv('data/french_words.csv')
dictionary = data.to_dict('records')


def change_word():
    global word, timer, language, index
    print(dictionary)
    window.after_cancel(timer)
    canvas.delete(word)
    canvas.delete(language)
    canvas.create_image(400, 263, image=old_image)
    canvas.itemconfig(new_image, image=old_image)
    language = canvas.create_text(400, 100, text='French', font=('Arial', 40, "italic"))
    index = random.randint(0, 100)
    word = canvas.create_text(400, 263, text=dictionary[index]['French'], font=('Arial', 40, "bold"))
    timer = window.after(3000, show_english_word)

def insert_unknown_word():
    with open('words_to_learn.csv', 'a') as file:
        file.write(dictionary[index]['French']+','+dictionary[index]['English']+'\n')
    change_word()

def right_word():
    dictionary.remove(dictionary[index])
    change_word()

def show_english_word():
    global word, language, index
    canvas.delete(word)
    canvas.delete(language)
    canvas.create_image(400, 263, image=new_image)
    canvas.itemconfig(old_image, image=new_image)
    language = canvas.create_text(400, 100, text='English', font=('Arial', 40, "italic"), fill='white')
    word = canvas.create_text(400, 263, text=dictionary[index]['English'], font=('Arial', 40, "bold"), fill='white')
    # canvas.itemconfig(language, fill='white', text='English')
    # canvas.itemconfig(word, fill='white', text=data['English'].iloc[index])


# ---------------------------- UI DESIGN ---------------------------- #

window = Tk()
window.config(width=1000, height=1000, padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title('Flashy')
canvas = Canvas(width=800, height=525, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=1, column=1, columnspan=2)

old_image = PhotoImage(file="images/card_front.png")
new_image = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 263, image=old_image)
language = canvas.create_text(400, 100, text='French', font=('Arial', 40, "italic"))

timer = window.after(3000, show_english_word)

# print(data)
# print(dictionary[0])
# del dictionary[0]
# print(dictionary)

index = random.randint(0, 100)
word = canvas.create_text(400, 263, text=dictionary[index]['French'], font=('Arial', 40, "bold"))

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=insert_unknown_word)
wrong_button.grid(row=2, column=1)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=change_word)

right_button.grid(row=2, column=2)

window.mainloop()

# language = Label(text="Title", justify=CENTER,font=('Arial', 40, "italic"), bg='white')
# language.place(x=340, y=100)

# french_word = Label(text='word', justify=CENTER, font=('Arial', 60, "bold"), bg='white')
# french_word.place(x=300, y=263)
