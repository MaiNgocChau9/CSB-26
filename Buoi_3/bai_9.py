class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

students = [
    Student("Alice", 8),
    Student("Bob", 7),
    Student("Charlie", 9)
]

total = sum([s.score for s in students])
print(total / len(students))