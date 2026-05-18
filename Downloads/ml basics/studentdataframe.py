import pandas as pd
students = {
    "Name": ["Arun", "Meera", "Rahul", "Anu", "Vishnu"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 90, 78, 92, 88]
}
df = pd.DataFrame(students)
print("Student DataFrame:")
print(df)
print("\nFirst 3 Rows:")
print(df.head(3))
print("\nShape of DataFrame:")
print(df.shape)