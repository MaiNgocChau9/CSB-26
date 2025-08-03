class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        return "Woof! Woof!"

dog_1 = Dog("Buddy", 3)
dog_2 = Dog("Max", 5)
print(f"{dog_1.name} is {dog_1.age} years old and says {dog_1.bark()}")