from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score Label
        self.score_label = Label(text=f'Score: {self.quiz.score}', bg=THEME_COLOR, fg='white', font=('Arial', 13))
        self.score_label.grid(pady=20, row=1, column=2)

        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.canvas.grid(pady=50, row=2, column=1, columnspan=2)
        self.question_text = self.canvas.create_text(150,
                                                     130,
                                                     width=280,
                                                     fill=THEME_COLOR,
                                                     font=('Arial', 20, "italic"))

        # Right and Wrong Button
        right_image = PhotoImage(file='images/true.png')
        self.right = Button(padx=20, pady=20, image=right_image, highlightthickness=0, command=self.right_check, bd=0)
        self.right.grid(row=3, column=1)

        wrong_image = PhotoImage(file='images/false.png')
        self.wrong = Button(padx=20, pady=20, image=wrong_image, highlightthickness=0, command=self.wrong_check, bd=0)
        self.wrong.grid(row=3, column=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            qtext = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=qtext)
        else:
            self.canvas.itemconfig(self.question_text, text="You've completed the quiz")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")

    def right_check(self):
        is_right = self.quiz.check_answer(True)
        self.give_feedback(is_right)

    def wrong_check(self):
        is_right = self.quiz.check_answer(False)
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
            self.quiz.score += 1
            self.score_label.config(text=f'Score: {self.quiz.score}')
        else:
            self.canvas.config(bg='red')

        self.window.after(1000, self.get_next_question)
