# CUSTOMER CHURN DATASET - EDA
# Using NumPy, Pandas and Matplotlib

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# 1. Create Dataset
# --------------------------------------------------

data = {
    "CustomerID": [
        "CUST001","CUST002","CUST003","CUST004","CUST005",
        "CUST006","CUST007","CUST008","CUST009","CUST010",
        "CUST011","CUST012","CUST013","CUST014","CUST015",
        "CUST016","CUST017","CUST018","CUST019","CUST020",
        "CUST021","CUST022","CUST023","CUST024","CUST025",
        "CUST026","CUST027","CUST028","CUST029","CUST030",
        "CUST031","CUST032","CUST033","CUST034","CUST035",
        "CUST036","CUST037","CUST038","CUST039","CUST040",
        "CUST041","CUST042","CUST043","CUST044","CUST045",
        "CUST046","CUST047","CUST048","CUST049","CUST050",
        "CUST051","CUST052","CUST053","CUST054","CUST055",
        "CUST056","CUST057","CUST058","CUST059","CUST060",
        "CUST061","CUST062","CUST063","CUST064","CUST065",
        "CUST066","CUST067","CUST068","CUST069","CUST070",
        "CUST071","CUST072","CUST073","CUST074","CUST075",
        "CUST076","CUST077","CUST078","CUST079","CUST080",
        "CUST081","CUST082","CUST083","CUST084","CUST085",
        "CUST086","CUST087","CUST088","CUST089","CUST090",
        "CUST091","CUST092","CUST093","CUST094","CUST095",
        "CUST096","CUST097","CUST098","CUST099","CUST100",
        "CUST011","CUST021"
    ],

    "Gender": [
        "Male","Female","Male","Male","Male","Female","Male","Male",
        "Male","Female","Male","Male","Male","Male","Female","Male",
        "Female","Female","Female","Male","Female","Male","Female",
        "Female","Female","Female","Female","Female","Female","Female",
        "Male","Male","Female","Female","Female","Male","Female","Male",
        "Male","Male","Male","Male","Female","Female","Female","Female",
        "Female","Male","Female","Female","Male","Female","Male","Female",
        "Male","Female","Female","Male","Male","Male","Male","Male",
        "Male","Male","Female","Male","Female","Female","Female","Female",
        "Female","Male","Female","Male","Female","Male","Female","Male",
        "Female","Male","Female","Male","Female","Male","Male","Male",
        "Female","Male","Female","Female","Female","Female","Female","Female",
        "Female","Female","Female","Male","Female"
    ],

    "Age": [
        35,43,61,51,27,53,31,48,65,32,25,31,40,57,38,33,62,35,64,70,
        41,43,42,62,58,46,32,62,18,42,24,26,41,18,61,np.nan,41,28,68,
        34,25,52,52,50,22,59,56,58,45,24,26,25,29,51,50,65,40,41,54,
        52,61,57,39,44,52,18,52,54,64,31,20,18,22,43,31,56,44,26,32,
        43,59,30,68,49,56,66,69,49,21,47,54,40,56,62,32,60,46,53,30,
        25,41
    ],

    "Tenure": [
        32,71,59,28,66,42,45,62,57,6,28,28,44,30,62,62,1,27,62,3,
        70,72,27,9,62,37,51,44,24,59,32,52,62,58,52,12,39,2,3,56,
        59,2,2,54,1,19,2,53,44,32,70,32,68,55,56,17,38,24,69,70,
        11,16,59,70,3,20,59,36,19,67,19,20,71,52,33,40,39,1,11,57,
        50,23,31,42,7,16,60,2,1,48,12,69,37,32,9,19,48,3,20,24,
        28,70
    ],

    "MonthlyCharges": [
        60.45,108.78,105.09,113.56,98.53,86.9,78.07,np.nan,114.01,
        117.37,48.39,50.54,68.56,64.84,119.45,37.59,21.81,69.39,
        37.88,56.65,94.42,92.09,50.81,74.25,70.88,np.nan,45.05,
        78.99,117.89,68.67,110.61,63.44,55.01,84.51,86.89,106.42,
        43.02,69.92,77.2,96.86,24.36,119.46,66.99,47.96,108.35,
        94.77,115.31,53.08,75.28,77.23,118.03,27.53,50.57,39.09,
        46.85,68.53,57.27,59.47,104.42,113,27.04,40.89,87.11,55.86,
        45.42,49.53,52.26,104.87,33.66,90.89,75.28,49.65,61.98,45.62,
        81.15,28.16,20.52,82.79,39.43,27.09,59.68,25.08,108.66,22.76,
        77.89,63.85,87.2,52.82,35.5,118.18,103.89,106.04,45.03,23.88,
        50.33,73.71,52.67,102.79,47.15,116.53,48.39,94.42
    ],

    "TotalCharges": [
        1902.06,7557.37,6373.08,3030.42,6438.35,3609.44,3681.62,
        3375.23,6512.78,807.94,1323.95,1298.14,3005.84,2097.91,
        7344.32,2474.2,47.68,1996.78,2370.43,121.51,6773.29,6653,
        1388.51,749.01,4486.98,3175.6,2162.48,3411.84,2763.71,
        3973.62,3452.31,3231.78,3444.21,4951.02,4518.12,1234.44,
        1805.33,130.68,325.31,5367.23,1478.61,373.13,0,2524.33,
        167.72,1921.91,250.93,2818.2,3473.38,2598.76,8175.24,892.6,
        3474.78,2321.81,2710.21,1154.65,2198.27,1238.89,7301.84,
        7974.57,418.66,639.84,5152.29,3862.07,21.45,930.37,2901.41,
        3866.78,422.05,6292.84,1253.91,1142.99,4309.77,2428.34,
        2602.71,1293.77,804.65,190.16,441.33,1579.43,3045.61,
        523.97,3240.43,825.76,550.31,972.74,5017.41,156.93,0,
        5556.61,1242.52,7226.75,1678.36,961.51,415.06,1294.53,
        2546.31,230.85,945.38,2828.28,1323.95,6773.29
    ],

    "Contract": [
        "Month-to-month","Two year","Month-to-month","Month-to-month",
        "One year","Month-to-month","Month-to-month","Two year",
        "One year","Month-to-month","Month-to-month","Month-to-month",
        "One year","Month-to-month","Month-to-month","Month-to-month",
        "Month-to-month","One year","Month-to-month","Two year",
        "Month-to-month","Month-to-month","Month-to-month","Month-to-month",
        "Two year","One year","Month-to-month","One year","Month-to-month",
        "One year","Month-to-month","One year","Month-to-month","Month-to-month",
        "Month-to-month","Month-to-month","Month-to-month","Month-to-month",
        "Two year","Month-to-month","Month-to-month","One year","Two year",
        "Month-to-month","Month-to-month","One year","Month-to-month",
        "Two year","Two year","Month-to-month","Month-to-month","Two year",
        "Month-to-month","Month-to-month","One year","One year","Two year",
        "Two year","One year","One year","Two year","One year","One year",
        "Month-to-month","Two year","Two year","One year","Month-to-month",
        "Month-to-month","Month-to-month","Month-to-month","Month-to-month",
        "Month-to-month","One year","One year","Two year","Month-to-month",
        "One year","Month-to-month","One year","Month-to-month","Month-to-month",
        "Two year","Month-to-month","Month-to-month","One year","Two year",
        "Month-to-month","Month-to-month","Two year","Month-to-month",
        "One year","One year","Month-to-month","Month-to-month","Month-to-month",
        "One year","Two year","One year","Month-to-month","One year",
        "Month-to-month","Month-to-month"
    ],

    "InternetService": [
        "Fiber optic","DSL","Fiber optic","Fiber optic","Fiber optic",
        "Fiber optic","DSL","DSL","DSL","No","No","Fiber optic","No",
        "Fiber optic",np.nan,"Fiber optic","DSL","DSL","Fiber optic",
        "Fiber optic","DSL","No","Fiber optic","DSL","No","No","No","DSL",
        "Fiber optic","Fiber optic","Fiber optic","No","Fiber optic","No",
        "No","No","Fiber optic","DSL","Fiber optic","No","DSL","Fiber optic",
        "DSL","Fiber optic","No","No","DSL","No","Fiber optic","Fiber optic",
        "Fiber optic","Fiber optic","Fiber optic","Fiber optic","DSL","DSL",
        "Fiber optic","Fiber optic","No",np.nan,"Fiber optic","Fiber optic",
        "No","Fiber optic","DSL","Fiber optic","No","Fiber optic","DSL",
        "Fiber optic","Fiber optic","No","No","No","Fiber optic","DSL","No",
        "Fiber optic","DSL","DSL","DSL","DSL","No","No","Fiber optic",
        "Fiber optic","DSL","No","No","DSL","Fiber optic","DSL","DSL",
        "Fiber optic","DSL","No","Fiber optic","DSL","No","Fiber optic",
        "No","DSL"
    ],

    "Churn": [
        "No","Yes","No","Yes","No","Yes","Yes","Yes","No","No","No","Yes",
        "No","Yes","Yes","Yes","No","Yes","No","No","Yes","Yes","Yes","Yes",
        "No","No","No","No","No","No","No","No","No","Yes","Yes","No","No",
        "Yes","No","Yes","No","Yes","Yes","Yes","No","Yes","No","Yes","No",
        "Yes","Yes","No","No","No","No","No","Yes","No","No","No","No","No",
        "No","No","Yes","No","No","No","Yes","Yes","No","No","No","No","Yes",
        "No","No","Yes","No","Yes","No","No","Yes","Yes","Yes","Yes","No","Yes",
        "No","Yes","No","No","Yes","No","No","No","No","No","No","Yes","No","No",
        "No","Yes"
    ]
}

df = pd.DataFrame(data)

# --------------------------------------------------
# 2. Display Dataset
# --------------------------------------------------

print("FIRST 5 RECORDS")
print(df.head())

print("\nDATASET SHAPE")
print(df.shape)

# --------------------------------------------------
# 3. Check Missing Values
# --------------------------------------------------

print("\nMISSING VALUES BEFORE CLEANING")
print(df.isnull().sum())

# Handle missing numerical values using median
df["Age"] = df["Age"].fillna(df["Age"].median())
df["MonthlyCharges"] = df["MonthlyCharges"].fillna(
    df["MonthlyCharges"].median()
)

# Handle missing categorical values using mode
df["InternetService"] = df["InternetService"].fillna(
    df["InternetService"].mode()[0]
)

print("\nMISSING VALUES AFTER CLEANING")
print(df.isnull().sum())

# --------------------------------------------------
# 4. Remove Duplicate Records
# --------------------------------------------------

print("\nDUPLICATE RECORDS BEFORE REMOVAL")
print(df.duplicated().sum())

df = df.drop_duplicates()

print("\nDATASET SHAPE AFTER REMOVING DUPLICATES")
print(df.shape)

# --------------------------------------------------
# 5. Summary Statistics
# --------------------------------------------------

print("\nSUMMARY STATISTICS")
print(df.describe())

# --------------------------------------------------
# 6. Churn Analysis
# --------------------------------------------------

print("\nCHURN COUNT")
print(df["Churn"].value_counts())

print("\nCHURN PERCENTAGE")
print(df["Churn"].value_counts(normalize=True) * 100)

# --------------------------------------------------
# 7. Average Values Based on Churn
# --------------------------------------------------

print("\nAVERAGE VALUES BY CHURN")
print(
    df.groupby("Churn")[[
        "Age",
        "Tenure",
        "MonthlyCharges",
        "TotalCharges"
    ]].mean()
)

# --------------------------------------------------
# 8. Contract vs Churn
# --------------------------------------------------

print("\nCONTRACT VS CHURN")
print(pd.crosstab(df["Contract"], df["Churn"]))

# --------------------------------------------------
# 9. Internet Service vs Churn
# --------------------------------------------------

print("\nINTERNET SERVICE VS CHURN")
print(pd.crosstab(df["InternetService"], df["Churn"]))

# --------------------------------------------------
# 10. Correlation Matrix
# --------------------------------------------------

print("\nCORRELATION MATRIX")
print(
    df[[
        "Age",
        "Tenure",
        "MonthlyCharges",
        "TotalCharges"
    ]].corr()
)

# --------------------------------------------------
# 11. Visualization - Churn
# --------------------------------------------------

plt.figure(figsize=(7,5))

df["Churn"].value_counts().plot(kind="bar")

plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# --------------------------------------------------
# 12. Visualization - Contract vs Churn
# --------------------------------------------------

pd.crosstab(
    df["Contract"],
    df["Churn"]
).plot(kind="bar", figsize=(8,5))

plt.title("Contract Type vs Customer Churn")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# --------------------------------------------------
# 13. Visualization - Monthly Charges
# --------------------------------------------------

plt.figure(figsize=(8,5))

df.groupby("Churn")["MonthlyCharges"].mean().plot(
    kind="bar"
)

plt.title("Average Monthly Charges by Churn")
plt.xlabel("Churn")
plt.ylabel("Average Monthly Charges")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# --------------------------------------------------
# 14. Visualization - Internet Service vs Churn
# --------------------------------------------------

pd.crosstab(
    df["InternetService"],
    df["Churn"]
).plot(kind="bar", figsize=(8,5))

plt.title("Internet Service vs Customer Churn")
plt.xlabel("Internet Service")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

print("\nEDA COMPLETED SUCCESSFULLY!")

Comment:-
FIRST 5 RECORDS
  CustomerID  Gender  Age  Tenure  MonthlyCharges  ...
0    CUST001    Male   35      32           60.45
1    CUST002  Female   43      71          108.78
2    CUST003    Male   61      59          105.09
3    CUST004    Male   51      28          113.56
4    CUST005    Male   27      66           98.53

DATASET SHAPE
(102, 9)

MISSING VALUES BEFORE CLEANING
CustomerID          0
Gender              0
Age                 1
Tenure              0
MonthlyCharges     2
TotalCharges        0
Contract            0
InternetService     2
Churn               0

DUPLICATE RECORDS BEFORE REMOVAL
2

DATASET SHAPE AFTER REMOVING DUPLICATES
(100, 9)
