word = input("Your word: ")
dict = {}

for i in word:
    dict[i] = 0

for i in word:
    dict[i] += 1

for letter in dict: 
    print(letter,"->",dict[letter])