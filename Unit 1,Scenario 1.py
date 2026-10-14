# Employee Management System using OOP

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def get_category(self):
        if self.salary >= 70000:
            return "High Salary"
        elif self.salary >= 40000:
            return "Medium Salary"
        else:
            return "Low Salary"

    def display(self):
        print("\nEmployee ID :", self.emp_id)
        print("Name        :", self.name)
        print("Salary      : ₹", self.salary)
        print("Category    :", self.get_category())


class Company:
    def __init__(self):
        self.employee_list = []

    def add_employee(self):
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        salary = float(input("Enter Salary: ₹"))

        employee = Employee(emp_id, name, salary)
        self.employee_list.append(employee)

        print("\nEmployee Added Successfully!")

    def display_employee(self):
        if len(self.employee_list) == 0:
            print("\nNo Employee Records Found!")
        else:
            print("\n------ Employee Details ------")
            for emp in self.employee_list:
                emp.display()


# Main Program

company = Company()

while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        company.add_employee()

    elif choice == 2:
        company.display_employee()

    elif choice == 3:
        print("\nThank You!")
        break

    else:
        print("\nInvalid Choice! Try Again.")
    Comment:-
  ===== Employee Management System =====
1. Add Employee
2. Display Employees
3. Exit

Enter your choice: 1

Enter Employee ID: E101
Enter Employee Name: Krishu
Enter Salary: ₹75000

Employee Added Successfully!

Enter your choice: 2

------ Employee Details ------

Employee ID : E101
Name        : Krishu
Salary      : ₹ 75000.0
Category    : High Salary
