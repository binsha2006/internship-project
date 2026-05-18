import pandas as pd
students = {
    "Name": ["Arun", "Meera", "Rahul", "Anu", "Vishnu"],
    "Marks": [85, 90, 78, 92, 60]
}
df = pd.DataFrame(students)
df["Grade"] = df["Marks"].apply(
    lambda x: "A" if x >= 90 else "B" if x >= 75 else "C"
)
print(df)