class Student:
    def __init__(self,name, age, grade) -> None:
        self.name = name
        self.age = age
        self.grade = grade #0..100
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self,name, max_students) -> None:
        self.name = name
        self.max_students = max_students
        self.students = []
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        print("Max size reached, cannot add student to this course")
        return False
    def get_average_grade(self):
        value = 0
        for s in self.students:
            value+= s.get_grade( )
        return value/len(self.students)


s1= Student("Sory", 10,99)
s2 = Student("Baha", 22, 75)
s3 = Student("Maha", 33,63)

course = Course("MDI", 2)

course.add_student(s1)
course.add_student(s2)
#print(course.get_average_grade())
course.add_student(s3)
print(course.get_average_grade())