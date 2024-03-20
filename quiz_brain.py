# Import the 'html' module to handle HTML entities in text.
import html

# Define the QuizBrain class to manage quiz functionality.
class QuizBrain:

    # Constructor method to initialize a new QuizBrain object with a list of questions.
    def __init__(self, q_list):
        self.question_number = 0  # Tracks the number of questions asked so far.
        self.score = 0  # Tracks the score of correctly answered questions.
        self.question_list = q_list  # Stores the list of all questions.
        self.current_question = None  # Holds the current question being asked.

    # Method to check if there are still unanswered questions in the quiz.
    def still_has_questions(self):
        # Returns True if the current question number is less than the total number of questions, False otherwise.
        return self.question_number < len(self.question_list)

    # Method to move to the next question in the list and format it for display.
    def next_question(self):
        # Retrieve the next question from the question list and update the current question.
        self.current_question = self.question_list[self.question_number]
        # Increment the question number counter.
        self.question_number += 1
        # Unescape any HTML entities in the question text for safe display.
        q_text = html.unescape(self.current_question.text)
        # Return the formatted question text.
        return f"Q.{self.question_number}: {q_text}"
        # The following line is commented out, but it shows how you might prompt the user for an answer.
        # user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        # self.check_answer(user_answer)

    # Method to check if the user's answer to the current question is correct.
    def check_answer(self, user_answer):
        # Retrieve the correct answer for the current question.
        correct_answer = self.current_question.answer
        # Compare the user's answer to the correct answer, ignoring case differences.
        if user_answer.lower() == correct_answer.lower():
            # If the answer is correct, increment the score.
            self.score += 1
            # Return True to indicate the answer was correct.
            return True
        else:
            # Return False to indicate the answer was incorrect.
            return False
