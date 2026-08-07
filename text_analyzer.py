sentence = input("Your sentence: ")
sentence_words = sentence.split()
words_numbers = len(sentence_words)

def find_tallest(sentence_words):
    tallest = ""
    sum = 0
    for i in sentence_words:
        if len(i) > sum:
            sum = len(i)
            tallest = i
    return tallest


tallest = find_tallest(sentence_words)

print("Total character: ", len(sentence))
print("Total word: ", words_numbers)
print("First word: ", sentence_words[0])
print("Last word: ", sentence_words[words_numbers - 1])
print("Tallest word: ", tallest)
print("Capitalized form: ", sentence.upper())