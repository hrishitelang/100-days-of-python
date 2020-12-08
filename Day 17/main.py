from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in range(len(question_data)):
    question_bank.append(Question(question_data[i]['text'], question_data[i]['answer']))

# print(question_bank)
# print(question_bank[0].text)
# print(question_bank[0].answer)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
