import csv
import sys

# Check command-line argument
if len(sys.argv) != 2:
    print("Usage: python employee.py employee.csv")
    exit()

filename = sys.argv[1]

# Display all employee records
def display_employees():
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)

        print("\n----- Employee Records -----")
        for row in reader:
            print("Employee ID :", row[0])
            print("Name        :", row[1])
            print("Department  :", row[2])
            print("Salary      :", row[3])
            print("-" * 30)

# Search employee by ID
def search_employee():
    emp_id = input("Enter Employee ID: ")
    found = False

    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if row[0] == emp_id:
                print("\nEmployee Found")
                print("Employee ID :", row[0])
                print("Name        :", row[1])
                print("Department  :", row[2])
                print("Salary      :", row[3])
                found = True
                break

    if not found:
        print("Employee Record Not Found.")

# Main Menu
while True:
    print("\n1. Display All Employees")
    print("2. Search Employee")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        display_employees()
    elif choice == "2":
        search_employee()
    elif choice == "3":
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")
Comment:-
1. Display All Employees
2. Search Employee
3. Exit
Enter Choice: 1

----- Employee Records -----
Employee ID : E101
Name        : Rahul
Department  : HR
Salary      : 30000
------------------------------
Employee ID : E102
Name        : Priya
Department  : IT
Salary      : 45000
------------------------------
