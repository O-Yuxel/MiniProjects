exam_notes = {}

while True:
    student = input("Öğrenci adı: ")

    if student == "q" and len(exam_notes) == 0:
        print("Henüz hiç kimse girmediniz.")
        pass
    elif student == "q":
        break
    else:
        note = int(input("Notu: "))
        exam_notes[student] = note

total = 0

for students, notes in exam_notes.items():
    print(students,"->", notes, "\n")
    total += notes

print("Sınıf Ortalaması: ", total/len(exam_notes))