import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "student": ["Ali", "Ayşe", "Mehmet", "Zeynep", "Can", "Elif", "Mert", "Derya",
                "Burak", "Selin", "Emre", "Ceren"],
    "class": ["A", "A", "B", "B", "A", "A", "B", "B", "A", "B", "A", "B"],
    "math": [72, 85, 91, 64, 78, 95, 58, 88, 76, 90, 69, 84],
    "physics": [68, 82, 89, 70, 75, 92, 61, 84, 73, 87, 65, 81],
    "python": [80, 90, 95, 72, 83, 98, 65, 91, 79, 94, 71, 88]
}

df = pd.DataFrame(data)


print("----------PART 1----------")

df["average"] = df[["math", "physics", "python"]].mean(axis=1)
print(df.head())


print("\n----------PART 2----------")

a_b_grouped = df.groupby("class")[["math", "physics", "python"]].mean()
print(a_b_grouped)


print("\n----------PART 3----------")

plt.figure()

classes_x = np.arange(len(a_b_grouped.loc["A"]))
width = 0.25

plt.bar(classes_x - width, a_b_grouped.loc["A"],width, color="red", label="A")
plt.bar(classes_x + width, a_b_grouped.loc["B"],width, color="blue", label="B")
plt.xticks(classes_x, a_b_grouped.columns)
plt.title("A vs B Class Performance")
plt.xlabel("Lessons")
plt.ylabel("Mean Grades")
plt.legend()
plt.grid(True)

plt.show()


print("\n----------PART 4----------")

mask_a = df["class"] == "A"
class_a = df[mask_a]

mask_b = df["class"] == "B"
class_b = df[mask_b]

plt.figure()

plt.scatter(class_a["python"], class_a["math"], color="red", label="A")
plt.scatter(class_b["python"], class_b["math"], color="blue", label="B")
plt.title("Scatter of Python and Math")
plt.xlabel("Python")
plt.ylabel("Math")
plt.legend()
plt.grid(True)

plt.show()


print("\n----------PART 5----------")

sorted_df = df.sort_values(by="average", ascending=False)
best5_students = sorted_df.head()

plt.figure()

plt.bar(best5_students["student"], best5_students["average"], color="green")
plt.title("Top 5 Students")
plt.xlabel("Student")
plt.ylabel("Average Grade")
plt.grid(True)

plt.show()


print("\n----------PART 6----------")

fig, axes = plt.subplots(2, 2, figsize=(12,8))

a_b_average = df.groupby("class")["average"].mean()

axes[0,0].bar(classes_x - width, a_b_grouped.loc["A"],width, color="red", label="A")
axes[0,0].bar(classes_x + width, a_b_grouped.loc["B"],width, color="blue", label="B")
axes[0,0].set_xticks(classes_x, a_b_grouped.columns)
axes[0,0].set_title("A vs B Class Performance")
axes[0,0].set_xlabel("Lessons")
axes[0,0].set_ylabel("Mean Grades")
axes[0,0].grid(True)

axes[0,1].scatter(class_a["python"], class_a["math"], color="red", label="A")
axes[0,1].scatter(class_b["python"], class_b["math"], color="blue", label="B")
axes[0,1].set_title("Scatter of Python and Math")
axes[0,1].set_xlabel("Python")
axes[0,1].set_ylabel("Math")
axes[0,1].grid(True)

axes[1,0].bar(best5_students["student"], best5_students["average"], color="green")
axes[1,0].set_title("Top 5 Students")
axes[1,0].set_xlabel("Student")
axes[1,0].set_ylabel("Average Grade")
axes[1,0].grid(True)

axes[1,1].bar(a_b_average.index, a_b_average.values)
axes[1,1].set_title("Average of Classes")
axes[1,1].set_xlabel("Classes")
axes[1,1].set_ylabel("Average Grade")
axes[1,1].grid(True)

fig.tight_layout()
fig.legend()

plt.show()