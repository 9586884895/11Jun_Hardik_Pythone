# 13.	Write a Python program to show hierarchical inheritance.
class Animal:
    def speak(self):
        print("Animals can make sounds.")

class Dog(Animal):
    def bark(self):
        print("Dog says: Woof!")

class Cat(Animal):
    def meow(self):
        print("Cat says: Meow!")

class Cow(Animal):
    def moo(self):
        print("Cow says: Moo!")

dog = Dog()
cat = Cat()
cow = Cow()

dog.speak()
dog.bark()

cat.speak()
cat.meow()

cow.speak()
cow.moo()