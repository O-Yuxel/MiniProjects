import pandas as pd

students = pd.DataFrame({
    "student_id": [101, 102, 103, 104, 105],
    "name": ["Ali", "Ayşe", "Mehmet", "Zeynep", "Can"],
    "class": ["12A", "12B", "12A", "12B", "12A"]
})

grades = pd.DataFrame({
    "student_id": [101, 102, 103, 104, 105],
    "math": [85, 92, 76, 95, 68],
    "physics": [78, 89, 82, 94, 71],
    "python": [90, 95, 88, 97, 65]
})


print("----------PART 1----------")

df = pd.merge(students, grades, on="student_id")
print(df)


print("\n----------PART 2----------")

df["average"] = (df["math"] + df["physics"] + df["python"]) / 3


print("\n----------PART 3----------")

new_students = pd.DataFrame({
    "student_id": [106, 107],
    "name": ["Elif", "Burak"],
    "class": ["12B", "12A"]
})

# df = pd.concat([df, new_students], ignore_index=True, axis=0)
# print(df)


print("\n----------PART 4----------")

new_grades = pd.DataFrame({
    "student_id": [106, 107],
    "math": [91, 79],
    "physics": [85, 75],
    "python": [93, 80]
})

new_data = pd.merge(new_students, new_grades, on="student_id")
df = pd.concat([df, new_data], ignore_index=True)
print(df)

print("\n----------BONUS----------")

df = df.fillna(df["average"].mean())


print("\n----------PART 5----------")

students = pd.DataFrame({
    "student_id" : [101, 102, 103, 104, 105],
    "name" : ["Ali", "Ayşe", "Mehmet", "Zeynep", "Can"] })

grades_missing = pd.DataFrame({
    "student_id" : [101, 102, 103, 104],
    "math": [85, 92, 76, 95],
    "physics": [78, 89, 82, 94],
    "python": [90, 95, 88, 97]
})

missing_grade_df = pd.merge(students, grades_missing, on="student_id", how="inner")
print(missing_grade_df)

missing_grade_df = pd.merge(students, grades_missing, on="student_id", how="left")
print(missing_grade_df)


print("\n----------PART 6----------")

best_students = df.sort_values(by="average",ascending=False)
best_student = best_students.iloc[0]["name"]
print(best_student)

worst_students = df.sort_values(by="average",ascending=True)
worst_student = worst_students.iloc[0]["name"]
print(worst_student)

mask = df["average"] > 85
above85_df = df[mask]
print(above85_df)

class_average_df = df.groupby("class")["average"].agg("mean")
print(class_average_df)