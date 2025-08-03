class Student:
    def __init__(self, name, score=0):
        self.name = name
        self.__score = score

    def update_score(self, score):
        self.__score = score

    def get_score(self):
        return self.__score

students_1 = Student("Alice", 8)
students_1.update_score(9)
print(f"{students_1.name} has a score of {students_1.get_score()}")
