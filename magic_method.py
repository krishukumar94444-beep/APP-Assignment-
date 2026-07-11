# Program to demonstrate Python Magic Methods
# Magic Methods Used: __init__, __add__, __eq__, __ge__

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Add marks of two students
    def __add__(self, other):
        return self.marks + other.marks

    # Compare equality of marks
    def __eq__(self, other):
        return self.marks == other.marks

    # Check greater than or equal to
    def __ge__(self, other):
        return self.marks >= other.marks


# Creating objects
student1 = Student("Krishu", 85)
student2 = Student("Rahul", 80)
student3 = Student("Aman", 85)

# __add__
print("Total Marks of Student1 and Student2:", student1 + student2)

# __eq__
print("Student1 and Student3 have equal marks:", student1 == student3)

# __ge__
print("Student1 has greater than or equal marks than Student2:", student1 >= student2)
