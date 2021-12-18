from question_model import Question
from data import question_data
from test_func import TestFunc

question_bank=[]
for question in question_data:
    question_text=question["question"]
    question_answer=question["correct_answer"]
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)

test=TestFunc(question_bank)
while test.still_has_questions():
    test.next_question()

if test.score >=7:
    print(f"Your final score is {test.score}/{test.question_number}")
    print("Congratulations , you have been selected to join Doodle ")
else:
    print(f"Your final score is {test.score}/{test.question_number}")
    print("Sorry , you were unable to clear the interview process. Better luck next time!")
