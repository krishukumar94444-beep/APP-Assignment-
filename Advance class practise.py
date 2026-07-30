# Advanced Class Concepts in Python

# Parent Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age      # Encapsulation

    def get_age(self):
        return self.__age

    def display(self):
        print("Name :", self.name)
        print("Age  :", self.__age)


# Child Class
class Student(Person):
    def __init__(self, name, age, roll, marks):
        super().__init__(name, age)
        self.roll = roll
        self.marks = marks

    # Method Overriding (Polymorphism)
    def display(self):
        super().display()
        print("Roll No :", self.roll)
        print("Marks   :", self.marks)

        if self.marks >= 90:
            grade = "A+"
        elif self.marks >= 75:
            grade = "A"
        elif self.marks >= 60:
            grade = "B"
        elif self.marks >= 40:
            grade = "C"
        else:
            grade = "Fail"

        print("Grade   :", grade)


# Another Child Class
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    # Method Overriding
    def display(self):
        super().display()
        print("Subject :", self.subject)


# -------- Main Program --------

print("====== Student Details ======")
s1 = Student("Krishu", 19, 65, 88)
s1.display()

print("\n====== Teacher Details ======")
t1 = Teacher("Rahul Sir", 35, "Python")
t1.display()

print("\nAge of Student :", s1.get_age())
Comment:-
====== Student Details ======
Name : Krishu
Age  : 19
Roll No : 65
Marks   : 88
Grade   : A

====== Teacher Details ======
Name : Rahul Sir
Age  : 35
Subject : Python

Age of Student : 19
