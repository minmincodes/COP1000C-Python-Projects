#
# Minh D Le
#
# quizGrade.py
#
# This application takes a set of data, the students test answers and compare them with the answer key, finding how many students got right or wrong and whether they passed or not.
#
# Function to read student answers from a file
def read_quiz_answers(file_path):
    try:
        # Attempt to open the file for reading
        with open(file_path, 'r') as file:
            # Read each line from the file, strip whitespace, and store in a list
            answers = [line.strip() for line in file]
            # Return the list of answers
            return answers
    except FileNotFoundError:
        # Handle the case where the specified file is not found
        print(f"Error: {file_path} file not found.")
        # Return None to indicate an error condition
        return None
    except Exception as e:
        # Handle unexpected errors and display an error message
        print(f"An unexpected error occurred: {e}")
        # Return None to indicate an error condition
        return None

# Function to grade a student's quiz based on key answers
def grade_quiz(student_name, key_answers, student_answers):
    correct_count = 0
    incorrect_count = 0
    incorrect_questions = []

    # Iterate through each question and compare student's answer with key answer
    for i in range(len(key_answers)):
        if key_answers[i] == student_answers[i]:
            correct_count += 1
        else:
            # If the answers don't match, increment incorrect count and record the question number
            incorrect_count += 1
            incorrect_questions.append(i + 1)

    # Display grading results for the student
    print(f"\nGrading for {student_name}:")
    print(f"Number of correct answers: {correct_count}")
    print(f"Number of incorrect answers: {incorrect_count}")

    # If there are incorrect answers, display the question numbers
    if incorrect_count > 0:
        print("Questions incorrectly answered: ", end="")
        print(", ".join(map(str, incorrect_questions)))

    # Determine and display the overall result (Passed or Failed)
    if correct_count >= 11:
        print("Result: Passed")
    else:
        print("Result: Failed")

# Main program
if __name__ == "__main__":
    # Define the correct answers key for the quiz
    quiz_key = ['A', 'C', 'A', 'B', 'B', 'D', 'D', 'A', 'C', 'A', 'B', 'C', 'D', 'D', 'B']

    # Continue grading students until the user decides to exit
    while True:
        # Prompt for student name and answers file
        student_name = input("Enter student name: ")
        answers_file = input("Enter name of student's answers file: ")

        # Call the function to read student answers from the file
        student_answers = read_quiz_answers(answers_file)

        # If answers are successfully read, proceed to grade the quiz
        if student_answers is not None:
            grade_quiz(student_name, quiz_key, student_answers)

        # Ask the user if they want to grade another student
        another_student = input("Would you like to grade another student? (y/n): ").lower()
        if another_student != 'y':
            # Break out of the loop if the user chooses not to grade another student
            break
