class Student:
    def __init__(self, name, grades=[]):
        self.name = name
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)
    
    def calculate_average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0
    
class GradeManager:
    def __init__(self, students=[]):
        self.students = students

    def add_student(self, name):
        self.students.append(Student(name, []))

    def record_grade(self, name, grade):
        for student in self.students:
            if student.name == name:
                student.add_grade(grade)
                return
        print(f"Student {name} not found.")
    
    def calculate_average_all(self):
        sum_averages = 0
        for student in self.students:
            sum_averages += student.calculate_average()
        return sum_averages / len(self.students) if self.students else 0

    def save_data(self, filename):
        with open(f"{filename}.txt", 'w') as file:
            for student in self.students:
                print(student.name, student.calculate_average(), student.grades)
                file.write(f"{student.name}: {student.calculate_average()}\n")
        print("Data saved successfully.")
        pass


while True:
    print("""
1. Add a new student
2. Record a grade for a student
3. Calculate the average grade of all students
4. Save the data to a file
5. Exit
         """)
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        GradeManager().add_student(input("Enter student name: "))
    elif choice == '2':
        name = input("Enter student name: ")
        grade = float(input("Enter grade: "))
        GradeManager().record_grade(name, grade)
    elif choice == '3':
        print(f"Average grade of all students: {GradeManager().calculate_average_all()}")
    elif choice == '4':
        filename = input("Enter filename to save data: ")
        GradeManager().save_data(filename)
    elif choice == '5':
        print("Exiting the program.")
        break