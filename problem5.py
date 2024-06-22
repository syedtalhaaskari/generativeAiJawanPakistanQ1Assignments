"""
Given the dict

students = {
    "Alice": {
                "Subjects": ["Math", "Science", "English"],
                "Scores": [85, 90, 78],
                "Class": 10
            },
    "Bob": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [75, 80, 88],
        "Class": 10
    },
    "Charlie": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [92, 89, 94],
        "Class": 11
    },
    "Diana": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [88, 76, 85],
        "Class": 11
    },
    "John": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [50, 60, 60],
        "Class": 11
    }
}

1. display Alice English Score
2. display Bob Class
3. display Charlie Math Score
4. display Diana's avg score
5. display John's all subject name and score with format: Student: [Name], Score: [Subject], Score: [Score].
6. Add new Student and its subject, score and class in same dict i.e students
7. add new subject and its score in John
"""

import pprint

print("Problem No. 5")

students = {
    "Alice": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [85, 90, 78],
        "Class": 10
    },
    "Bob": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [75, 80, 88],
        "Class": 10
    },
    "Charlie": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [92, 89, 94],
        "Class": 11
    },
    "Diana": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [88, 76, 85],
        "Class": 11
    },
    "John": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [50, 60, 60],
        "Class": 11
    }
}

print("\nStudents Dictionary:")
pprint.pp(students)

print(f"\nAlice English Score: {students['Alice']["Scores"][2]}")
print(f"\nBob Class: {students['Bob']["Class"]}")
print(f"\nAlice Math Score: {students['Charlie']["Scores"][0]}")

diana_average_score = 0
for score in students['Diana']['Scores']:
    diana_average_score += score

diana_average_score /= len(students['Diana']['Scores'])
print(f"\nDiana Average Score: {diana_average_score}")

student_name = "John"
stu_data = students[student_name]
for i in range(len(stu_data['Subjects'])):
    print(f"Student: {student_name}, Subject: {stu_data['Subjects'][i]}, Score: {stu_data['Scores'][i]}")
    
students['Talha'] = {
    "Subjects": ["Math", "Science", "English"],
    "Scores": [85, 90, 78],
    "Class": 10,
}

print("\nAfter new student addition:")
pprint.pp(students)

stu_data["Subjects"].append("Programming")
stu_data["Scores"].append(94)

print("\nAfter new subject addition in John:")
pprint.pp(students)