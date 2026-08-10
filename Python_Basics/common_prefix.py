def find_mutuals():
    words_raw = input("Kelimelerin: ")
    words = words_raw.split()
    n = 1
    mutual_letters = ""
    check = False

    while True:
        first_words_length = len(words[0])
        m = 0

        if n > first_words_length:
            break

        comparing_letters = words[0][0:n]

        for i in words:
            if comparing_letters == i[0:n]:
                m += 1

        if m == len(words):
            mutual_letters = comparing_letters
            check = True

        n += 1

    return mutual_letters, check

mutual_letters, check = find_mutuals()

if check:
    print("Ortak harfler şunlardır: ", mutual_letters)
else:
    print("Ortak başlangıç yok.")