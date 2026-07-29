# Employee Management System
class Employee:
    # Class Variable
    company_name = "TechNova Solutions"

    # Constructor
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    # Class Method
    @classmethod
    def change_company(cls, new_company):
        cls.company_name = new_company

    # Static Method
    @staticmethod
    def salary_category(salary):
        if salary >= 70000:
            return "High Salary"
        elif salary >= 40000:
            return "Medium Salary"
        else:
            return "Low Salary"

    # Magic Method
    def __str__(self):
        return (
            f"Employee ID : {self.emp_id}\n"
            f"Name        : {self.name}\n"
            f"Salary      : ₹{self.salary:,.2f}\n"
            f"Category    : {Employee.salary_category(self.salary)}"
        )


class Company:
    def __init__(self):
        self.employee_list = []

    # Add Employee
    def add_employee(self, employee):
        self.employee_list.append(employee)

    # Display Employees
    def display_employees(self):
        print("=" * 50)
        print(f"        {Employee.company_name}")
        print("      EMPLOYEE MANAGEMENT SYSTEM")
        print("=" * 50)

        for count, employee in enumerate(self.employee_list, start=1):
            print(f"\nEmployee {count}")
            print("-" * 50)
            print(employee)

        print("\n" + "=" * 50)
        print("Total Employees :", len(self.employee_list))
        print("=" * 50)

# Main Program
company = Company()

emp1 = Employee(101, "Aarav Sharma", 85000)
emp2 = Employee(102, "Meera Patel", 55000)
emp3 = Employee(103, "Rohan Verma", 32000)

company.add_employee(emp1)
company.add_employee(emp2)
company.add_employee(emp3)

company.display_employees()

print("\nUpdating Company Name...\n")

Employee.change_company("NextGen Software Pvt. Ltd.")

company.display_employees()
Comment:-
        TechNova Solutions
      EMPLOYEE MANAGEMENT SYSTEM

Employee 1
Employee ID : 101
Name        : Aarav Sharma
Salary      : ₹85,000.00
Category    : High Salary

Employee 2
Employee ID : 102
Name        : Meera Patel
Salary      : ₹55,000.00
Category    : Medium Salary

Employee 3
Employee ID : 103
Name        : Rohan Verma
Salary      : ₹32,000.00
Category    : Low Salary

Total Employees : 3

Updating Company Name:

        NextGen Software Pvt. Ltd.
      EMPLOYEE MANAGEMENT SYSTEM


Employee 1

Employee ID : 101
Name        : Aarav Sharma
Salary      : ₹85,000.00
Category    : High Salary

Employee 2 
Employee ID : 102
Name        : Meera Patel
Salary      : ₹55,000.00
Category    : Medium Salary

Employee 3 
Employee ID : 103
Name        : Rohan Verma
Salary      : ₹32,000.00
Category    : Low Salary
Total Employees : 3
