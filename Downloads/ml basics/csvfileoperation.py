import pandas as pd
students = {
    "Name": ["Arun", "Meera", "Rahul", "Anu", "Vishnu"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 90, 78, 92, 88]
}

df = pd.DataFrame(students)
df.to_csv("students.csv", index=False)
print("CSV file created successfully!")
new_df = pd.read_csv("students.csv")
print("\nData from CSV:")
print(new_df)
print("\nColumn Names:")
print(new_df.columns)
print("\nData Types:")
print(new_df.dtypes)