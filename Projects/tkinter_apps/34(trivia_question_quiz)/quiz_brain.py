import html

from question_model import Question


class QuizBrain:

    def __init__(self, q_list: list[Question]):
        self.question_number: int = 0
        self.score: int = 0
        self.question_list: list[Question] = q_list
        self.current_question: Question = None

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def next_question(self) -> str:
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer) -> bool:
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
