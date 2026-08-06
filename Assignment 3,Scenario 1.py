import csv

# Function to display all patient records
def display_patients():
    with open("patients.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)

        print("\n----- Patient Records -----")
        for row in reader:
            print("Patient ID     :", row[0])
            print("Name           :", row[1])
            print("Treatment Cost :", row[2])
            print("Category       :", row[3])
            print("-" * 30)

# Function to search patient by ID
def search_patient():
    patient_id = input("Enter Patient ID: ")
    found = False

    with open("patients.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if row[0] == patient_id:
                print("\nPatient Found")
                print("Patient ID     :", row[0])
                print("Name           :", row[1])
                print("Treatment Cost :", row[2])
                print("Category       :", row[3])
                found = True
                break

    if not found:
        print("Patient Record Not Found.")

while True:
    print("\n1. Display All Patients")
    print("2. Search Patient")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        display_patients()
    elif choice == "2":
        search_patient()
    elif choice == "3":
        break
    else:
        print("Invalid Choice")
Comment:-
1. Display All Patients
2. Search Patient
3. Exit
Enter Choice: 1

----- Patient Records -----
Patient ID     : P101
Name           : Rahul
Treatment Cost : 5000
Category       : General
------------------------------
Patient ID     : P102
Name           : Priya
Treatment Cost : 8000
Category       : Special
------------------------------
Patient ID     : P103
Name           : Amit
Treatment Cost : 6500
Category       : General
------------------------------
Patient ID     : P104
Name           : Sneha
Treatment Cost : 9000
Category       : Special
------------------------------
1. Display All Patients
2. Search Patient
3. Exit
Enter Choice: 2

Enter Patient ID: P103

Patient Found
Patient ID     : P103
Name           : Amit
Treatment Cost : 6500
Category       : General
