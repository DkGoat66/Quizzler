# Importing the Question class from the question_model module
from question_model import Question

# Importing the question_data list from the data module
from data import question_data

# Importing the QuizBrain class
from quiz_brain import QuizBrain

# Importing the QuizInterface class for user interaction
from ui import QuizInterface

# Creating an empty list to store Question objects
question_bank = []

# Iterating through the question_data list to create Question objects
for question in question_data:
    # Extracting question text and correct answer from each dictionary in question_data
    question_text = question["question"]
    question_answer = question["correct_answer"]

    # Creating a new Question object and adding it to the question_bank list
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Creating a QuizBrain object with the question_bank list
quiz = QuizBrain(question_bank)

# Creating a QuizInterface object for user interaction, passing the quiz as an argument
quiz_ui = QuizInterface(quiz)

# The following code is commented out, suggesting it may not be needed or is a placeholder
# while quiz.still_has_questions():
#     quiz.next_question()

# Displaying a message indicating the completion of the quiz
print("You've completed the quiz")

# Displaying the final score of the user
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
