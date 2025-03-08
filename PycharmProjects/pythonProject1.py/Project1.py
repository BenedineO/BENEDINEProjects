

# Define a function to calculate the final grade

def calculate_final_grade():
    # Collecting student exam scores
    maths_exam_score = float(input("Enter the score for Maths Exam (out of 100): "))
    english_exam_score = float(input("Enter the score for English Exam (out of 100): "))
    physics_exam_score = float(input("Enter the score for Physics Exam (out of 100): "))

    # Calculate the average exam score
    average_exam_score = (maths_exam_score + english_exam_score + physics_exam_score) / 3

    # Collecting student homework scores
    maths_homework_score = float(input("Enter the score for Maths homework (out of 50): "))
    english_homework_score = float(input("Enter the score for English Homework (out of 50): "))
    physics_homework_score = float(input("Enter the score for Physics Homework (out of 50): "))

    # Calculate the average homework score
    average_homework_score = (maths_homework_score + english_homework_score + physics_homework_score) / 3

    # Calculate the weighted average of exam and homework scores
    final_grade = (0.6 * average_exam_score) + (0.4 * average_homework_score)

    # Print the final grade
    print(f"Final Grade: {final_grade}")

# Call the function to calculate the final grad
calculate_final_grade()


