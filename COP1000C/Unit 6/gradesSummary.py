#
# Minh D Le
#
# gradesSummary.py
#
# This application takes a set of data, specifically a grade sheet of students from a class room and averages out the grade as well as the passing percentage.
# The app also combs for passing and failing students
#

def get_valid_grade(line):
    try:
        # Convert the line to an integer and return it
        return int(line.strip())
    except ValueError:
        # Handle the case where the grade is not a valid integer
        print(f"Error: Invalid grade '{line.strip()}' for {previous_student_name}. Skipping this student.")
        return None


def process_course_file(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read course information
            course_number = file.readline().strip()
            instructor = file.readline().strip()
            term = file.readline().strip()

            # Display course information
            print("\n[Course Grades Summary Report]")
            print(f"\nName of course file: {file_path}\n")
            print(f" \n{'-' * 60} ")
            print(f"          Broward College Grades Summary          \n{'-' * 60}")
            print(f"\n{course_number} - {instructor}\nProfessor: {term}\n")
            print("\nStudent Name                 Grade")
            print("-" * 40)

            students_passed = 0
            students_failed = 0
            total_grade = 0
            total_students = 0

            global previous_student_name
            previous_student_name = ""

            # Read student data
            for line in file:
                student_name = line.strip()
                grade = get_valid_grade(file.readline())

                if grade is not None:
                    total_students += 1
                    total_grade += grade

                    # Display student name and grade
                    print(f"{student_name:<30}{grade}")

                    # Check if student passed or failed
                    if grade >= PASSING_GRADE:
                        students_passed += 1
                    else:
                        students_failed += 1

                    previous_student_name = student_name

            if total_students > 0:
                # Display students' performance summary
                print("\nStudents' Performance")
                print("-" * 30)
                print(f"Passed: {students_passed:<20}Failed: {students_failed}")
                print(f"Passing Percent: {students_passed / total_students * 100:.0f}%")
                print(f"Average Grade: {total_grade / total_students:.0f}")
            else:
                print("\nNo valid student records found.")

    except FileNotFoundError:
        # Handle the case where the file is not found
        print(f"Error: {file_path} file not found.")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Constants
    PASSING_GRADE = 60
    previous_student_name = ""

    while True:
        # Get file path from user
        file_path = input("Enter name of course file: ")
        process_course_file(file_path)

        # Ask user if they want to process another file
        another_file = input("Would you like to process another file (y/n)? ").lower()
        if another_file != 'y':
            break
