import pandas as pd

data = {
    "name": ["Ali", "Ayşe", "Mehmet", "Zeynep", "Can", "Elif", "Burak", "Deniz"],
    "age": [17, 18, 17, 18, 17, 18, 17, 18],
    "class": ["12A", "12B", "12A", "12B", "12A", "12B", "12A", "12B"],
    "math": [85, 92, 76, 95, 68, 88, 79, 91],
    "physics": [78, 89, 82, 94, 71, 85, 75, 90],
    "python": [90, 95, 88, 97, 65, 91, 80, 93]
}

df = pd.DataFrame(data)


print("----------PART 1----------")

first5_rows = df.head()
student_count = df.shape[0]
column_count = df.shape[1]
column_name = df.columns
column_type = df.dtypes

print("İlk beş sütun göründüğü gibidir: ", first5_rows)
print("Öğrenci sayısı: ", student_count)
print("Sütun sayısı: ", column_count)
print("Sütunların isimleri: ",column_name)
print("Sütunların türleri:\n",column_type, sep="")


print("\n----------PART 2----------")

name_column = df["name"]
math_column = df["math"]
mixed_columns = df[["name","math","python"]]

print("Sadece öğrencilerin isimlerinden, matematik notlarından ve python notlarından oluşan dataframe:\n", mixed_columns)


print("\n----------PART 3----------")


math_filtred_df = df.query("math > 80")
students_mfd = math_filtred_df["name"]

python_filtred_df = df.query("python >= 90")
students_pfd = python_filtred_df["name"]

two_filtred_df = df.query("math > 80 and python >= 90")
students_tfd = math_filtred_df["name"]

print("Matematik notu 80'in üzerinde olan öğrenciler:\n",students_mfd, "\n", sep="")
print("Python notu 90'ın üzerinde olan öğrenciler:\n",students_pfd, "\n", sep="")
print("Matematik notu 80'in üzerinde ve python notu 90'ın üzerinde olan öğrenciler:\n",students_tfd, sep="")


print("\n----------PART 4----------")

df["average"] = df[["math", "physics", "python"]].mean(axis=1)
print("Dataframe'e öğrencilerin ortalamasının eklemiş hali:", df, sep="")


print("\n----------PART 5----------")

sorted_df = df.sort_values("average", ascending=False)
print("Öğrencilerin ortalamalarına göre sıralanışı:\n",sorted_df[["name", "average"]], sep="")


print("\n----------PART 6----------")

math_mean = df["math"].mean()
physics_mean = df["physics"].mean()
python_mean = df["python"].mean()
max_math = df["math"].max()
min_python = df["python"].min()
succesful_student_count = len(df.query("average > 85"))

print("Matematik dersinin ortalaması: ", math_mean)
print("Physics dersinin ortalaması: ", physics_mean)
print("Python dersinin ortalaması: ", python_mean)
print("En yüksek matematik dersi: ", max_math)
print("En düşük python dersin: ", min_python)
print("Başarılı öğrencilerin sayısı: ", succesful_student_count)
