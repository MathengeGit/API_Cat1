# Online Course Management System
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade

    def display_grades(self):
        print(f"Grades for {self.name}:")
        for assignment, grade in self.assignments.items():
            print(f"- {assignment}: {grade}")


class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def assign_grade(self, student_id, assignment_name, grade):
        for student in self.students:
            if student.student_id == student_id:
                student.add_assignment(assignment_name, grade)
                print(f"Assigned {grade} for {assignment_name} to {student.name}")
                return
        print("Student not found.")

    def display_all_grades(self):
        print(f"Grades for {self.course_name}:")
        for student in self.students:
            student.display_grades()
            print("")

if __name__ == "__main__":
    instructor = Instructor("Dr. Smith", "Python 101")
    student1 = Student("Bob", "S001")
    student2 = Student("Carol", "S002")

    instructor.add_student(student1)
    instructor.add_student(student2)

    instructor.assign_grade("S001", "Assignment 1", 85)
    instructor.assign_grade("S002", "Assignment 1", 90)
    instructor.assign_grade("S001", "Assignment 2", 88)

    instructor.display_all_grades()
