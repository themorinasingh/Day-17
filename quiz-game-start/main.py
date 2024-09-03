from data import question_data
from question_model import Question
from quiz_brain import QuizBrain



#creating a question bank

question_bank = []

for i in range(len(question_data)):
    question_bank.append(Question(question_data[i]["question"], question_data[i]["correct_answer"]))

my_quiz = QuizBrain(question_bank)


while my_quiz.still_has_questions():
    my_quiz.next_question()

print("You have completed the quiz")
print(f"Your final score was {my_quiz.score}/{my_quiz.question_number}")