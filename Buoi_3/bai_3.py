class Student:
    def __init__(self, name, grade, points):
        self.name = name
        self.grade = grade
        self.points = points
    def is_passed(self):
        return self.points > 5
    
student_1 = Student("Alice", "10A", 8)
student_2 = Student("Bob", "10B", 4)
print(f"{student_1.name} in {student_1.grade} is {student_1.is_passed()}")