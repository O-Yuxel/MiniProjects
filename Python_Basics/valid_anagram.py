word1_raw = input("Birinci kelime: ")
word2_raw = input("İkinci kelime: ")

def is_anagram(word1_raw, word2_raw):
    if len(word1_raw) != len(word2_raw):
        return False
    else:
        word1_sorted = sorted(word1_raw)
        word2_sorted = sorted(word2_raw)
        
        if word1_sorted != word2_sorted:
            return False
        return True


check = is_anagram(word1_raw,word2_raw)

if check:
    print("Anagram!")
else:
    print("Anagram değil.")

# 2980XP