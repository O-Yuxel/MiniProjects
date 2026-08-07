numbers_raw = input("Sayılar: ")
numbers = numbers_raw.split()

repeating_numbers = []
only_one_numbers = []

numbers_count = {}

for i in numbers:
    numbers_count[i] = 0

for i in numbers:
    numbers_count[i] += 1


for number, count in numbers_count.items():
    if count > 1:
        repeating_numbers.append(number)
    else:
        only_one_numbers.append(number)   

if len(repeating_numbers) != 0:
    print("Tekrar eden sayıların listesi: ", repeating_numbers)
    print("Bir adet olan sayıların listesi: ", only_one_numbers)
else:
    print("Tekrar eden sayı yok.")