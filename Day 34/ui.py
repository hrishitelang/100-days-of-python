from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        #Score Label
        self.score = Label(text='Score: 0', bg=THEME_COLOR, fg='white', font=('Arial', 13))
        self.score.grid(pady=20, row=1, column=2)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.canvas.grid(pady=50, row=2, column=1, columnspan=2)
        self.question_text = self.canvas.create_text(150,
                                130,
                                text="Some Question Text",
                                fill=THEME_COLOR,
                                font=('Arial', 20, "italic"))

        #Right and Wrong Button
        right_image = PhotoImage(file='images/true.png')
        self.right = Button(padx=20, pady=20, image=right_image, highlightthickness=0, width=100, height=100)
        self.right.grid(row=3, column=1)

        wrong_image = PhotoImage(file='images/false.png')
        self.wrong = Button(padx=20, pady=20, image=wrong_image, highlightthickness=0, width=100, height=100)
        self.wrong.grid(row=3, column=2)
        self.window.mainloop()
