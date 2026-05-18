import pandas as pd
students = {
    "Name": ["Arun", "Meera", "Rahul", "Anu", "Vishnu"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 90, 78, 92, 88]
}
df = pd.DataFrame(students)
print("Students with marks above 80:")
print(df[df["Marks"] > 80])
print("\nStudents whose age is above 20:")
print(df[df["Age"] > 20])