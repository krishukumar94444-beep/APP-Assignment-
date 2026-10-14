
import numpy as np
import pandas as pd

# Student records
names = ["Amit", "Rahul", "Priya", "Sneha", "Rohan"]
marks = np.array([85, 72, 95, 68, 88])

# Calculate statistics using NumPy
mean_marks = np.mean(marks)
median_marks = np.median(marks)
maximum_marks = np.max(marks)
minimum_marks = np.min(marks)

# Create Pandas DataFrame
df = pd.DataFrame({
    "Student Name": names,
    "Marks": marks
})

# Display all student records
print("STUDENT MARKS ANALYSIS SYSTEM")
print("-" * 35)
print("\nAll Student Records:")
print(df.to_string(index=False))

# Display statistical analysis
print("\nMarks Analysis:")
print("Mean Marks:", mean_marks)
print("Median Marks:", median_marks)
print("Maximum Marks:", maximum_marks)
print("Minimum Marks:", minimum_marks)

# Display students scoring more than 80
print("\nStudents Scoring More Than 80 Marks:")
top_students = df[df["Marks"] > 80]
print(top_students.to_string(index=False))

Comment:-
STUDENT MARKS ANALYSIS SYSTEM

All Student Records:
Student Name  Marks
        Amit     85
       Rahul     72
       Priya     95
       Sneha     68
       Rohan     88

Marks Analysis:
Mean Marks: 81.6
Median Marks: 85.0
Maximum Marks: 95
Minimum Marks: 68

Students Scoring More Than 80 Marks:
Student Name  Marks
        Amit     85
       Priya     95
       Rohan     88
