import pandas as pd
students = {
    "Name": [
        "Arun", "Meera", "Rahul", "Anu", "Vishnu",
        "Akhil", "Sneha", "Kiran", "Diya", "Fathima"
    ],
    
    "Department": [
        "CSE", "ECE", "CSE", "MECH", "ECE",
        "CSE", "MECH", "ECE", "CSE", "MECH"
    ],
    
    "Marks": [85, 90, 78, 92, 88, 95, 70, 82, 91, 76],
    
    "Attendance": [80, 92, 70, 85, 60, 95, 72, 88, 90, 65]
}
df = pd.DataFrame(students)
print("Student DataFrame:")
print(df)
topper = df[df["Marks"] == df["Marks"].max()]
print("\nTopper:")
print(topper)
dept_average = df.groupby("Department")["Marks"].mean()
print("\nAverage Marks Department-wise:")
print(dept_average)
low_attendance = df[df["Attendance"] < 75]
print("\nStudents with Attendance below 75%:")
print(low_attendance)
sorted_df = df.sort_values(by="Marks", ascending=False)
print("\nStudents Sorted by Marks (Descending):")
print(sorted_df)