numbers = []

while True:
    number = input("Your number: ")
    if number != "q":
        numbers.append(int(number))
    elif len(numbers) == 0 and number == "q":
        print("Hiç sayı girilmedi.")
        pass
    else:
        break

print("Toplam sayı:", len(numbers))
print("Girilen sayılar:", numbers)
print("En büyük sayı:", max(numbers))
print("En küçük sayı:", min(numbers))
print("Toplam:", sum(numbers))
print("Ortalama:", sum(numbers)/len(numbers))