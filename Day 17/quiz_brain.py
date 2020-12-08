class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list


    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.question_number += 1
        answer = input(f"Q. {self.question_number}: {self.question_list[self.question_number - 1].text} "
                       f"(True/False): ")
        self.check_answer(answer, self.question_list[self.question_number - 1].answer)

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
            print(f"Score: ({self.score}/{len(self.question_list)})")
        else:
            print(f"You got it wrong! Score: ({self.score}/{len(self.question_list)})")
        print(f"The correct answer is {correct_answer}")
        print("\n")
