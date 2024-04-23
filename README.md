
This Python application is a quiz game called "Quizzler." Here's a breakdown of its components:
Components:
1. Question Model (question_model.py):
    * Defines a Question class to represent a single question in the quiz. Each question has text and an answer.
2. Data (data.py):
    * Retrieves quiz questions from an API using the requests library.
    * Defines the Question class which encapsulates the text and answer of a question.
3. Quiz Brain (quiz_brain.py):
    * Manages the quiz logic.
    * Tracks the current question number, score, and the list of questions.
    * Provides methods to check if there are remaining questions, get the next question, and check the user's answer.
4. User Interface (ui.py):
    * Implements the graphical user interface using Tkinter.
    * Displays the quiz question and keeps track of the user's score.
    * Provides buttons for the user to select true or false as their answer.
    * Gives visual feedback on whether the answer is correct or not.
Usage:
* The main.py script initializes the quiz by creating instances of the QuizBrain and QuizInterface classes.
* The QuizInterface class creates the GUI window, displays questions, handles user input, and updates the interface based on the user's answers.
* The QuizBrain class manages the quiz logic, including tracking the score and advancing to the next question.
Execution:
* To run the quiz, execute the main.py script.
* The user interacts with the quiz through the graphical interface, answering true or false to each question.
* After answering all questions, the final score is displayed.
This application demonstrates the use of object-oriented programming in Python to create a simple quiz game with a graphical user interface.




<img width="341" alt="Screenshot 2024-04-16 at 10 42 03" src="https://github.com/HesamFarjad/Quizzler-App/assets/81914229/dc6d934d-d301-4267-b450-1e1fdff72a0c">
<img width="276" alt="Screenshot 2024-04-16 at 10 50 48" src="https://github.com/HesamFarjad/Quizzler-App/assets/81914229/40d0928d-9351-42aa-8749-37c15e06c410">
<img width="273" alt="Screenshot 2024-04-16 at 10 51 09" src="https://github.com/HesamFarjad/Quizzler-App/assets/81914229/20a7c14b-b90a-42a1-a08e-67427663ecfc">
<img width="337" alt="Screenshot 2024-04-16 at 10 45 06" src="https://github.com/HesamFarjad/Quizzler-App/assets/81914229/941faa6a-54f0-4ec9-8e53-dabb7db76cb5">
