class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks


class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def course_average(self):
        count = 0
        for student in self.students:
            count += student.marks

            print (count / len(self.students))

# students instances
student_1 = Student("Evans", 20, 90)
student_2 = Student("Ryan", 19, 85)
student_3 = Student("Timothy", 21, 95)

# creting course instances
course1 = Course("Python")

# adding students to a course
course1.add_student(student_1)
course1.add_student(student_2)
course1.add_student(student_3)

# for student in course1.students:
#     print(student.name)

course1.course_average()