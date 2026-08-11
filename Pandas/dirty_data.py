import pandas as pd
import numpy as np

data = {
    "name": ["Ali", "Ayşe", "Mehmet", "Zeynep", "Can", "Ali", "Elif", None],
    "age": [17, 18, None, 17, 18, 17, None, 18],
    "class": ["12A", "12B", "12A", "12B", "12A", "12A", "12B", "12A"],
    "math": [85, 92, 76, None, 68, 85, 91, 78],
    "physics": [78, 89, 82, 94, None, 78, 85, 80],
    "python": [90, 95, 88, 97, 65, 90, None, 83]
}

df = pd.DataFrame(data)


print("----------PART 1----------")

nan_column_bool = df.isna().any(axis=0)
nan_column = df.columns[nan_column_bool]
nan_column_count = df.isna().sum()
nan_total = df.isna().sum().sum()

print("İçinde NaN olan_columnlar: ", nan_column)
print("Columnların NaN sayıları: ",nan_column_count)
print("Toplam NaN sayısı: ",nan_total)


print("\n----------PART 2----------")

df["age"] = df["age"].fillna(df["age"].mean())
df["math"] = df["math"].fillna(df["math"].mean())
df["physics"] = df["physics"].fillna(df["physics"].mean())
df["python"] = df["python"].fillna(df["python"].mean())


print("\n----------PART 3----------")

df = df.dropna(subset=["name"])


print("\n----------PART 4----------")

# print(df.duplicated())

df = df.drop_duplicates()
print(df)


print("\n----------PART 5----------")

mean_math = df["math"].mean()
mean_python = df["python"].mean()
mean_physics = df["physics"].mean()

print(mean_math, mean_physics, mean_python)


print("\n----------PART 6----------")

df["average"] = (df["math"] + df["physics"] + df["python"]) / 3
mask = df["average"] >= 85
print(df[mask]["name"])


print("\n----------PART 7----------")

student_count = df.shape[0]
column_count = df.shape[1]
nan_total2 = df.isna().sum().sum()

print(student_count)
print(column_count)
print(nan_total2)