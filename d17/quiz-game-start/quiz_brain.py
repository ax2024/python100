
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True/False)?: ")

        self.question_number += 1
        self.check_answer(answer, current_question.answer)

    def check_answer(self, user, correct):
        if user[0].lower() == correct[0].lower():
            self.score += 1
            print("Correct")
        else:
            print("Wrong")
        print(f"Your current score is: {self.score}/{self.question_number}\n")

    def result(self):
        print("You've completed the quiz")
        print(f"Your final score was: {self.score}/{self.question_number}")
