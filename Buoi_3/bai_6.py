class Animal:
    def make_sound(self):
        print("Sound")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

animal = Animal()
animal.make_sound()
cat = Cat()
cat.make_sound()