import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

students = {
    "Name": [
        "Arun", "Meera", "Rahul", "Anu", "Vishnu",
        "Akhil", "Sneha", "Kiran", "Diya", "Fathima"
    ],

    "Department": [
        "CSE", "ECE", "CSE", "MECH", "ECE",
        "CSE", "MECH", "ECE", "CSE", "MECH"
    ],

    "Marks": [85, 90, 78, 92, 88, 95, 70, 82, np.nan, 76],

    "Attendance": [80, 92, 70, 85, 60, 95, 72, 88, 90, np.nan]
}
df = pd.DataFrame(students)
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())
df["Result"] = df["Marks"].apply
(lambda x: "Pass" if x >= 40 else "Fail"
)
print("Summary Statistics:")
print(df.describe())
topper = df[df["Marks"] == df["Marks"].max()]
print("\nTopper:")
print(topper)
dept_avg = df.groupby("Department")["Marks"].mean()
print("\nDepartment-wise Average Marks:")
print(dept_avg)
df.to_csv("cleaned_students.csv", index=False)
print("\nCleaned dataset exported successfully!")
plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.show()
result_count = df["Result"].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(
    result_count,
    labels=result_count.index,
    autopct="%1.1f%%"
)
plt.title("Pass vs Fail")
plt.show()
plt.figure(figsize=(8, 5))
plt.hist(df["Marks"], bins=5)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()
print("\nFINAL ANALYSIS REPORT")
print("----------------------")
print("Total Students:", len(df))
print("Average Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())
print("\nStudents with Attendance below 75%:")
print(df[df["Attendance"] < 75][["Name", "Attendance"]])