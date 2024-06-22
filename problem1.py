"""
Create a dictionary named student_scores with the following key-value pairs:
"Alice": 85
"Bob": 78
"Charlie": 92
"Diana": 88
"Evan": 76


1. Write a for loop to iterate through the student_scores dictionary and print each student's name and their score in the format: Student: [Name], Score: [Score].

2. Write a for loop to calculate the average score of the students. Print the average score.

3. Write a for loop to assign grades based on the following criteria:
Score >= 90: Grade A
Score >= 80 and < 90: Grade B
Score >= 70 and < 80: Grade C
Score < 70: Grade D
Store these grades in a new dictionary called student_grades.

4. Modify the student_scores dictionary by adding 5 bonus points to each student's score. 
Print the updated student_scores dictionary.
"""

print("Problem No. 1")

student_scores = {
    "Bob": 78,
    "Charlie": 92,
    "Diana": 88,
    "Evan": 76,
}

print("\nStudent Dictionary:", student_scores, end="\n\n")

average_student_score = 0
student_grades = {}

for name, score in student_scores.items():
    print(f"Student: {name}, Score: {score}")

    average_student_score += score
    grade = ""
    
    if score <= 100 and score >= 90:
        grade = "A"
    elif score < 90 and score >= 80:
        grade = "B"
    elif score < 80 and score >= 70:
        grade = "C"
    elif score < 70 and score >= 60:
        grade = "D"
    elif score < 60 and score >= 0:
        grade = "F"
    else:
        grade = "Invalid Score"
    
    student_grades[name] = grade
    student_scores[name] += 5
    print(f"Grade: {grade}")

average_student_score /= len(student_scores)

print("\nAverage Student Score:", average_student_score)

print(f"\nAfter Adding Grace 5 Marks:\n{student_scores}")