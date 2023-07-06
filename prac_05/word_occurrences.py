"""
Word Occurrences
Estimate: 25 minutes
Actual:   60 minutes
"""
word_to_frequency = {}
sentence = input("Text: ")
words = sentence.split()

for word in words:
    try:
        word_to_frequency[word] += 1
    except KeyError:
        word_to_frequency[word] = 1



for word in word_to_frequency:
    print(f"{word}: {word_to_frequency[word]}")
