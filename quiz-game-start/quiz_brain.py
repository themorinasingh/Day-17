
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        users_answer = input(f"Q.{self.question_number}): {question.text} (True/False): ").title()
        self.check_answer(users_answer, question.answer)
        print(f"Current Score: {self.score}/{self.question_number}")

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print("You got it wrong")

        print(f"The correct answer: {correct_answer}")


    def still_has_questions(self):
        return self.question_number < len(self.question_list)



