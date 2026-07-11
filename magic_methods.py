class Student:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch

    def __str__(self):
        return f"Student Name: {self.name}\nBranch: {self.branch}"

    def __len__(self):
        return len(self.name)


student = Student("Krishu", "CSE")

print(student)
print("Characters in name:", len(student))
