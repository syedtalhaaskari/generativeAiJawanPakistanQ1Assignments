"""
In this exercise, you will create a Python class named Student to represent students. 
The class should have the following attributes and methods:

Attributes:

name: instance variable
age: instance variable
courses: instance variable
available_courses: class variable -> possible values ["English", "Urdu", "Physics", "Math", "Chemistry"]

Methods:

display_info(): An instance method that displays the student's name and age.
enroll(): An instance method that allows a student to enroll in a course by adding it to their list of enrolled courses.
list_courses(): An instance method that displays all the courses that student is enrolled
list_available_courses(): An instance method that display all the avaiable courses


1. Create three instances of the Student class with different names and ages.

2. enroll the students in courses by calling the enroll method.
make sure student should only enroll in the course that are listing in available course
i.e if user input the course "Islamyat" then program should not allow it

3. call list_courses
4. call list_available_courses

"""

class Student:
    available_courses = ["English", "Urdu", "Physics", "Math", "Chemistry"]

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.courses = []
        
    def display_info(self):
        print(f"\nName: {self.name}, Age: {self.age}")
        
    def enroll(self):
        course = input(f"\n{self.name} please enter the course name: ")

        if course in Student.available_courses:
            if course in self.courses:
                print("You are already enrolled in this course")
            else:
                self.courses.append(course)
                print(f"You are successfully enrolled in the {course} course")
        else:
            print(f"Course {course} is not available.")
        
    def list_courses(self):
        print(f"\nEnrolled Courses - {self.name}:")
        for (i, course) in enumerate(self.courses):
            print(f"{i + 1}. {course}")
        
    def list_available_courses(self):
        available_courses = [course for course in Student.available_courses if course not in self.courses]

        if len(available_courses) == 0:
            print(f"\n{self.name} you are already enrolled in all of the available courses.")
        else:
            print(f"\nAvailable Courses - {self.name}:")
            for (i, course) in enumerate(available_courses):
                print(f"{i + 1}. {course}")
                
student1 = Student("Talha", 27)
student2 = Student("Asif", 26)
student3 = Student("Shayan", 25)

student1.display_info()
student2.display_info()
student3.display_info()

student1.enroll()
student2.enroll()
student3.enroll()

student1.list_courses()
student2.list_courses()
student3.list_courses()

student1.list_available_courses()
student2.list_available_courses()
student3.list_available_courses()
