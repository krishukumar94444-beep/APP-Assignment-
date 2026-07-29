# Employee Class
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    # Find Employee Category
    def get_category(self):
        if self.salary >= 70000:
            return "High Salary"
        elif self.salary >= 40000:
            return "Medium Salary"
        else:
            return "Low Salary"


# Company Class
class Company:
    def __init__(self):
        self.employees = []

    # Add Employee
    def add_employee(self, employee):
        self.employees.append(employee)

    # Display Employees
    def display_employees(self):
        print("\n------ Employee Details ------")
        for employee in self.employees:
            print("Employee ID :", employee.emp_id)
            print("Name        :", employee.name)
            print("Salary      : ₹", employee.salary)
            print("Category    :", employee.get_category())
            print("------------------------------")


# Main Program
company = Company()

n = int(input("Enter number of employees: "))

for i in range(n):
    print("\nEnter Employee", i + 1, "Details")
    emp_id = input("Employee ID: ")
    name = input("Name: ")
    salary = float(input("Salary: ₹"))

    employee = Employee(emp_id, name, salary)
    company.add_employee(employee)

company.display_employees()
Comment:-
Enter number of employees: 3

Enter Employee 1 Details
Employee ID: E101
Name: Rahul
Salary: ₹35000

Enter Employee 2 Details
Employee ID: E102
Name: Priya
Salary: ₹50000

Enter Employee 3 Details
Employee ID: E103
Name: Amit
Salary: ₹80000

------ Employee Details ------
Employee ID : E101
Name        : Rahul
Salary      : ₹ 35000.0
Category    : Low Salary
------------------------------
Employee ID : E102
Name        : Priya
Salary      : ₹ 50000.0
Category    : Medium Salary
------------------------------
Employee ID : E103
Name        : Amit
Salary      : ₹ 80000.0
Category    : High Salary
------------------------------
