from data import question_data, question_data2
from question_model import Question
from quiz_brain import QuizBrain


def main() -> None:
    question_bank: list[Question] = []

    for question in question_data2:
        question_text = question['question']
        question_answer = question['correct_answer']
        new_question = Question(text=question_text, answer=question_answer)
        question_bank.append(new_question)

    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions():
        quiz.next_question()

    print("You've completed the quiz.")
    print(f"Your final score is: {quiz.score}/{quiz.question_number}")


if __name__ == '__main__':
    main()
