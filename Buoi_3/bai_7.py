class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

class Teacher(Person):
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject

    def teach(self):
        return f"{self.name} is teaching {self.subject}"

person = Person("Alice", 25)
print(person.introduce())

teacher = Teacher("John Doe", 30, "Mathematics")
print(teacher.teach())
print(teacher.introduce())