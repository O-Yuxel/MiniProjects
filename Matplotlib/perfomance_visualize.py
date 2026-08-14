import matplotlib.pyplot as plt
import numpy as np

students = ["Ali", "Ayşe", "Mehmet", "Zeynep", "Can", "Elif", "Mert", "Derya"]
math = [72, 85, 91, 64, 78, 95, 58, 88]
physics = [68, 82, 89, 70, 75, 92, 61, 84]
python = [80, 90, 95, 72, 83, 98, 65, 91]

print("----------PART 1----------")

plt.figure()

plt.bar(students, math, color= "red")
plt.title("Mathematics Grades")
plt.xlabel("Students")
plt.ylabel("Grade")
plt.grid(True)

plt.show()


print("\n----------PART 2----------")

students_x = np.arange(len(students))
width = 0.25

plt.figure()

plt.bar(students_x  - width, math, width, color="cyan", label="math")
plt.bar(students_x, physics, width, color="blue", label="physics")
plt.bar(students_x  + width, python, width, color="green", label="python")

plt.xticks(students_x, students)
plt.title("All Grades")
plt.xlabel("Students")
plt.ylabel("Grade")
plt.grid(True)
plt.legend()

plt.show()


print("\n----------PART 3----------")

plt.figure()

plt.scatter(math, python, alpha=0.7)
plt.title("Math vs Python")
plt.xlabel("Math grade")
plt.ylabel("Python grade")
plt.grid(True)

plt.show()


print("\n----------PART 4----------")

plt.figure()

plt.hist(math, bins=5, alpha=0.7)
plt.title("Distribution of Math Grades")
plt.xlabel("Grade")
plt.ylabel("Number of Student")
plt.grid(True)

plt.show()


print("\n----------PART 5----------")

plt.figure()

plt.plot(students, math, label="math", color="cyan")
plt.plot(students, physics, label="physics", color="blue")
plt.plot(students, python, label="python", color="black")

plt.title("All Grades")
plt.xlabel("Students")
plt.ylabel("Grades")
plt.grid(True)
plt.legend()

plt.show()


print("\n----------PART 6----------")

fig, axes = plt.subplots(2, 2, figsize=(12,8))

axes[0][0].set_title("Math Grades")
axes[0][0].set_xlabel("Students")
axes[0][0].set_ylabel("Math")
axes[0][0].grid()
axes[0][0].bar(students, math, color="cyan", label="Math Bar")

axes[0][1].set_title("Math vs Python")
axes[0][1].set_xlabel("Math")
axes[0][1].set_ylabel("Python")
axes[0][1].grid()
axes[0][1].scatter(math, python, color="green", label="Math vs Python", alpha=0.7)

axes[1][0].set_title("Math Grades")
axes[1][0].set_xlabel("Math")
axes[1][0].set_ylabel("Student")
axes[1][0].grid()
axes[1][0].hist(math, color="red", label="Math Hist", bins=5)

axes[1][1].set_title("All Grades")
axes[1][1].set_xlabel("Students")
axes[1][1].set_ylabel("Grades")
axes[1][1].grid()

axes[1][1].plot(students, math, color="red", label="Math Line")
axes[1][1].plot(students, physics, color="green", label="Physics Line")
axes[1][1].plot(students, python, color="blue", label="Python Line")

fig.tight_layout()
fig.legend()
plt.show()


print("\n----------PART 7----------")

print("Analysis 1: Elif has the highest math grade.")
print("Analysis 2: Math and Python grades show a positive relationship.")
print("Analysis 3: Most scores are concentrated around the middle-to-high range.")

plt.figure()

plt.bar(students, math, color= "red")
max_math_grade = math.index(max(math))
plt.bar(max_math_grade, max(math), color="black")
plt.title("Who is the greatest in math?")
plt.xlabel("Students")
plt.ylabel("Grade")
plt.grid(True)

plt.show()