def find_longest(words):
    max = 0
    longest = ""

    for i in words:
        if len(i) > max:
            max = len(i)
            longest = i  
    return longest

def find_smallest(words):
    min = len(words[0])
    smallest = ""

    for i in words:
        if len(i) <= min:
            min = len(i)
            smallest = i  
    return smallest

def find_most_repeating(words):
    words_counts = {}
    max = 0 
    most_repeating = ""

    for i in words:
        words_counts[i] = 0

    for i in words:
        words_counts[i] += 1

    for word, count in words_counts.items():
        if count > max:
            max = count
            most_repeating = word

    return most_repeating, max


sentence = input("Cümlen: ")

words = sentence.split()
total_word = len(words)
print("Toplam kelime sayısı: ", total_word)


longest = find_longest(words)
smallest = find_smallest(words)

print("En uzun kelime: ", longest)
print("En kısa kelime: ", smallest)


most_repeating, count_of_most_repeating = find_most_repeating(words)
print("En çok geçen kelime: ", most_repeating, f"({count_of_most_repeating})")


reverse_words = reversed(words)
print("Ters çevrilmiş cümle: " ,end=" ")
for i in reverse_words:
    print(i, end=" ")


alphabetic_words = sorted(words)
print("\nAlfabetik sıralı kelimeler: ", alphabetic_words)

# STRING EXPLORER 1 | 1280 XP