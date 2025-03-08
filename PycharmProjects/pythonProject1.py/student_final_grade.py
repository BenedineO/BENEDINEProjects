# ---------------------GROUP 1 --------PROJECT 1 --------------------
# Creating a python program that calculates final grade for a student based on exam and homework scores.

# Student biology exam score
biology_exam_score = float(input("Enter biology exam score (out of 100): "))
if biology_exam_score > 100 or biology_exam_score < 0:   # To validate maximum score range
    print("Please enter the score that is between 0 and 100")
    exit()  # To exit the code

# Student biology homework score
biology_homework_score = float(input("Enter biology homework score (out of 50): "))
if biology_homework_score > 50 or biology_homework_score < 0:  # To validate maximum score range
    print("Please enter the score that is between 0 and 50")
    exit()  # To exit the code

# Student chemistry exam score (out of 100)
chemistry_exam_score = float(input("Enter chemistry exam score: "))
if chemistry_exam_score > 100 or chemistry_exam_score < 0:  # To validate maximum score range
    print("Please enter the score that is between 0 and 100")
    exit()  # To exit the code

# Prompt user for chemistry homework score (out of 50)
chemistry_homework_score = float(input("Enter chemistry homework score: "))
if chemistry_homework_score > 50 or chemistry_homework_score < 0:  # To validate maximum score range
    print("Please enter the score that is between 0 and 50")
    exit()  # To exit the code

# Calculate weighted biology exam score (60% of final grade)
weighted_biology_exam_score = (biology_exam_score / 100) * 60

# Calculate weighted biology homework score (40% of final grade)
weighted_biology_homework_score = (biology_homework_score / 50) * 40

# Calculate weighted chemistry exam score (60% of final grade)
weighted_chemistry_exam_score = (chemistry_exam_score / 100) * 60

# Calculate weighted chemistry homework score (40% of final grade)
weighted_chemistry_homework_score = (chemistry_homework_score / 50) * 40

# Calculate final biology grade
final_biology_grade = weighted_biology_exam_score + weighted_biology_homework_score

# Calculate final chemistry grade
final_chemistry_grade = weighted_chemistry_exam_score + weighted_chemistry_homework_score

# Calculate overall final grade (average of biology and chemistry)
overall_final_grade = (final_biology_grade + final_chemistry_grade) / 2

# Print final grades
print("Final Biology Grade:", final_biology_grade)
print("Final Chemistry Grade:", final_chemistry_grade)
print("Overall Final Grade:", overall_final_grade)

# -----------------THANK YOU------------------------

