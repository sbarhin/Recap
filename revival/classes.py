class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_name(self):
        return self.name

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_avg_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)


student1 = Student("Tim", 13, 87)
student2 = Student("Jill", 14, 80)
course = Course("science", 3)
course.add_student(student1)
course.add_student(student2)
print(Student.get_name(student1), "-", Student.get_grade(student1))
print(Student.get_name(student2), "-", Student.get_grade(student2))
print(course.get_avg_grade())
