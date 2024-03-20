# Importing all names from the tkinter module for GUI creation.
from tkinter import *
# Importing the QuizBrain class from the quiz_brain module to manage quiz functionality.
from quiz_brain import QuizBrain
# A constant for the theme color used in the GUI.
THEME_COLOR = "#375362"

# Define the QuizInterface class to create the GUI for the quiz.
class QuizInterface:
    # Constructor method to initialize the QuizInterface object with a QuizBrain object.
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # Setting up the main window.
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Creating and placing the score label in the window.
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=0)

        # Creating and placing the canvas for question text.
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, width=280, text="Some Question Text", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Creating and placing the "true" button.
        true_image = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.correct_button.grid(row=2, column=0)

        # Creating and placing the "false" button.
        false_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.wrong_button.grid(row=2, column=1)

        # Fetching the first question.
        self.get_next_question()

        # Main loop to run the tkinter window.
        self.window.mainloop()

    # Method to fetch and display the next question, or end the quiz if there are no more questions.
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the questions.")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    # Method called when the "true" button is pressed.
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    # Method called when the "false" button is pressed.
    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    # Method to provide visual feedback for whether the answer was correct.
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        # Calls get_next_question after a short delay.
        self.window.after(1000, self.get_next_question)
