from question_model import Question
from quiz_brain import QuizBrain
from data import question_data
from ui import QuizInterface


def main() -> None:
    question_bank: list[Question] = []

    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    quiz = QuizBrain(question_bank)
    quiz_ui = QuizInterface(quiz)
    while quiz.still_has_questions():
        quiz.next_question()

    print("You've completed the quiz")
    print(f"Your final score is: {quiz.score}/{quiz.question_number}")


if __name__ == '__main__':
    main()
