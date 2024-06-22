"""
Givent the list of students
students = [
    {
        "name": "Alice",
        "subjects": ["Math", "Science", "English"],
        "scores": [85, 90, 78],
        "Class": 10
    },
    {
        "name": "Bob",
        "subjects": ["Math", "Science", "English"],
        "scores": [75, 80, 88],
        "Class": 10
    },
    {
        "name": "Charlie",
        "subjects": ["Math", "Science", "English"],
        "scores": [92, 89, 94],
        "Class": 11
    },
    {
        "name": "Diana",
        "subjects": ["Math", "Science", "English"],
        "scores": [88, 76, 85],
        "Class": 11
    }
    {
        "name": "John",
        "subjects": ["Math", "Science", "English"],
        "scores": [50, 60, 60],
        "Class": 11
    }
]

1. display Alice English Score
2. display Bob Class
3. display Charlie Math Score
4. display Diana's avg score
5. display John's all subject name and score with format: Student: [Name], Score: [Subject], Score: [Score].
6. display which class obtained the higher marks
7. display the student name that obtain high marks in subject Math in class 10
8. Add new Student and its subject, score and class in same dict i.e students
"""

import pprint

print("Problem No. 6")

students = [
    {
        "name": "Alice",
        "subjects": ["Math", "Science", "English"],
        "scores": [85, 90, 78],
        "Class": 10
    },
    {
        "name": "Bob",
        "subjects": ["Math", "Science", "English"],
        "scores": [75, 80, 88],
        "Class": 10
    },
    {
        "name": "Charlie",
        "subjects": ["Math", "Science", "English"],
        "scores": [92, 89, 94],
        "Class": 11
    },
    {
        "name": "Diana",
        "subjects": ["Math", "Science", "English"],
        "scores": [88, 76, 85],
        "Class": 11
    },
    {
        "name": "John",
        "subjects": ["Math", "Science", "English"],
        "scores": [50, 60, 60],
        "Class": 11
    },
]

print("\nStudents List:")
pprint.pp(students)

print(f"\nAlice English Score: {students[0]["scores"][2]}")
print(f"\nBob Class: {students[1]["Class"]}")
print(f"\nAlice Math Score: {students[2]["scores"][0]}")

diana_average_score = 0
for score in students[3]['scores']:
    diana_average_score += score

diana_average_score /= len(students[3]['scores'])
print(f"\nDiana Average Score: {diana_average_score}")

stu_ind = 4
student = students[stu_ind]
for i in range(len(student['subjects'])):
    print(f"Student: {stu_ind}, Subject: {student['subjects'][i]}, Score: {student['scores'][i]}")

class_marks = {}
highest_math_score = 0
highest_math_student_name = ''

for student in students:
    marks = sum(student["scores"])
    class_marks[student["Class"]] = {
        "count": class_marks[student["Class"]]["count"] + 1 if student["Class"] in class_marks else 1,
        "total_marks": class_marks[student["Class"]]["total_marks"] + marks if student["Class"] in class_marks else marks,
    }
    class_marks[student["Class"]]["average"] = int(class_marks[student["Class"]]["total_marks"] / class_marks[student["Class"]]["count"])
    
    if student["Class"] == 10 and student["scores"][0] > highest_math_score:
        highest_math_score = student["scores"][0]
        highest_math_student_name = student["name"]

highest_score_class = 0
highest_score = 0

for _class, data in class_marks.items():
    if data["average"] > highest_score:
        highest_score_class = _class
        highest_score = data["average"]

print(f"\nHighest Score Class: {highest_score_class}, Highest Score: {highest_score}")

print(f"\nHighest Math Score Student: {highest_math_student_name}, Highest Score: {highest_math_score}")

new_student = {
    "name": "Talha",
    "subjects": ["Math", "Science", "English"],
    "scores": [100, 100, 99],
    "Class": 11
}

students.append(new_student)

print("\nAfter adding a new student:")
pprint.pprint(students)