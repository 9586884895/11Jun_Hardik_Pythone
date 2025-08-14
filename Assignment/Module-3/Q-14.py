#14.Write a Python program to show hybrid inheritance.
class Person:
    def info(self):
        print("This is a person.")
#Single Inheritance
class Student(Person):
    def student_info(self):
        print("This is a student.")

#Hierarchical Inheritance
class Teacher(Person):
    def teacher_info(self):
        print("This is a teacher.")

#Multiple Inheritance
class TeachingAssistant(Student, Teacher):
    def ta_info(self):
        print("This is a teaching assistant.")

# Creating object of Last Class
ta = TeachingAssistant()

# Accessing methods from all parent classes
ta.info()            # From Person
ta.student_info()    # From Student
ta.teacher_info()    # From Teacher
ta.ta_info()         # Own method