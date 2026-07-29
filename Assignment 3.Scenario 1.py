# Patient Class
class Patient:
    def __init__(self, patient_id, name, treatment_cost, category):
        self.patient_id = patient_id
        self.name = name
        self.treatment_cost = treatment_cost
        self.category = category


# Hospital Class
class Hospital:
    def __init__(self):
        self.patients = []

    # Add Patient
    def add_patient(self, patient):
        self.patients.append(patient)

    # Display All Patients
    def display_patients(self):
        print("\n------ Patient Records ------")
        for patient in self.patients:
            print("Patient ID      :", patient.patient_id)
            print("Name            :", patient.name)
            print("Treatment Cost  : ₹", patient.treatment_cost)
            print("Category        :", patient.category)
            print("-----------------------------")


# Main Program
hospital = Hospital()

n = int(input("Enter number of patients: "))

for i in range(n):
    print("\nEnter Patient", i + 1, "Details")
    patient_id = input("Patient ID: ")
    name = input("Name: ")
    treatment_cost = float(input("Treatment Cost: ₹"))
    category = input("Category (General/Special): ")

    patient = Patient(patient_id, name, treatment_cost, category)
    hospital.add_patient(patient)

hospital.display_patients()
Comment:-
Enter number of patients: 1

Enter Patient 1 Details
Patient ID: 101
Name: Harry 
Treatment Cost: ₹50000
Category (General/Special): general

------ Patient Records ------
Patient ID      : 101
Name            : Harry 
Treatment Cost  : ₹ 50000.0
Category        : general
-----------------------------
