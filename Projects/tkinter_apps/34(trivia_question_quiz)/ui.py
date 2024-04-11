import tkinter

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = tkinter.Tk()
        self.window.title("Quizzler")
        self.window.config(padx= 20, pady= 20, bg=THEME_COLOR)
        
        self.canvas = tkinter.Canvas(width=300, height=250, bg='white',  highlightthickness=0)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="Test",
                                                     font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        
        self.scoreboard = tkinter.Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.scoreboard.grid(column=1, row=0)
        
        false_photo = tkinter.PhotoImage(file='images/false.png')
        self.false_button = tkinter.Button(image=false_photo,highlightthickness=0, bd=0, command=self.pressed_false)
        self.false_button.grid(column=1, row=2)
        
        true_photo = tkinter.PhotoImage(file='images/true.png')
        self.true_button = tkinter.Button(image=true_photo, highlightthickness=0, bd=0, command=self.pressed_true)
        self.true_button.grid(column=0, row=2)
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def get_next_question(self) -> None:
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.scoreboard.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.scoreboard.config(text=f"score: {self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def pressed_true(self) -> None:
        self.give_feedback(self.quiz.check_answer("true"))
        
    def pressed_false(self) -> None:
        is_correct = self.quiz.check_answer("false")
        self.give_feedback(is_correct)
        
    def give_feedback(self, is_correct: bool) -> None:
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
            
        self.window.after(1000, self.get_next_question)
        
        
    