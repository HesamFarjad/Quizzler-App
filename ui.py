from tkinter import *

import quiz_brain
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="Some questions", fill=THEME_COLOR, font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.score_label = Label(text="Score = 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        true_image = PhotoImage(file="./images/true.png")
        self.g_button = Button(image=true_image, highlightthickness=0, command=self.clicked_green)
        self.g_button.grid(row=2, column=1)

        false_image = PhotoImage(file="./images/false.png")
        self.r_button = Button(image=false_image, highlightthickness=0, command=self.clicked_red)
        self.r_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached end of the quiz")
            self.g_button.config(state="disabled")
            self.r_button.config(state="disabled")

    def clicked_green(self):
        print("green pressed")
        self.give_feedback(self.quiz.check_answer('True'))

    def clicked_red(self):
        print("red pressed")
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="#009051")
        else:
            self.canvas.config(bg="#C1103E")
        self.window.after(1000, self.get_next_question)

