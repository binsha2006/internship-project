import pandas as pd
import numpy as np
students = {
    "Name": ["Arun", "Meera", "Rahul", "Anu", "Vishnu"],
    "Age": [20, 21, np.nan, 22, 20],
    "Marks": [85, np.nan, 78, 92, 88]
}
df = pd.DataFrame(students)
print("Original DataFrame:")
print(df)
print("\nMissing Values:")
print(df.isnull())
filled_df = df.fillna({
    "Age": df["Age"].mean(),
    "Marks": df["Marks"].mean()
})
print("\nDataFrame after filling missing values:")
print(filled_df)
dropped_df = df.dropna()
print("\nDataFrame after removing missing rows:")
print(dropped_df)