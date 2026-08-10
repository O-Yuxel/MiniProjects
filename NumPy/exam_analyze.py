import numpy as np

grades = np.array([
    [85, 90, 78],
    [70, 88, 95],
    [92, 81, 76],
    [60, 75, 89],
    [99, 94, 91]
])

print("----------PART 1----------")

student_count = grades.shape[0]
lesson_count =  grades.shape[1]
mean_note = np.mean(grades)
max_note = np.max(grades)
min_note = np.min(grades)


print("Toplam öğrenci sayısı: ", student_count)
print("Toplam ders sayısı", lesson_count)
print("Tüm notların ortalaması", mean_note)
print("En yüksek not", max_note)
print("En düşük not", min_note)


print("\n----------PART 2----------")

students_mean = np.mean(grades, axis=1)
n = 1
for i in students_mean:
    print(f"Öğrenci {n}:", i)
    n += 1


print("\n----------PART 3----------")

lessons_name = ["Türkçe", "Matematik", "Fen"]
lessons_mean = np.mean(grades, axis=0)
for lesson, mean in zip(lessons_name, lessons_mean):
    print(lesson, ":", mean)

print("\n----------PART 4----------")

best_student = np.argmax(students_mean) + 1
print(f"En yüksek not ortalamasına sahip {best_student}. öğrencidir. Not ortalaması {np.max(students_mean)}'dır. ")


print("\n----------PART 5----------")

hard_lesson = np.argmin(lessons_mean) 
print(f"En zor ders {lessons_name[hard_lesson]}. Not ortalaması {np.min(lessons_mean)}. ")