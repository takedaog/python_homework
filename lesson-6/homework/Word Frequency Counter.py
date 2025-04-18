import os
import string
from collections import Counter

if not os.path.exists("sample.txt"):
    with open("sample.txt", "w") as f:
        text = input("Enter a paragraph: ")
        f.write(text)

with open("sample.txt", "r") as f:
    words = f.read().lower()
    for p in string.punctuation:
        words = words.replace(p, "")
    words = words.split()

word_count = Counter(words)
total_words = sum(word_count.values())
top_n = input("How many top words to show? ")
top_n = int(top_n) if top_n.isdigit() else 5

print("Total words:", total_words)
print(f"Top {top_n} most common words:")
for word, count in word_count.most_common(top_n):
    print(f"{word} - {count} times")

with open("word_count_report.txt", "w") as f:
    f.write("Word Count Report\n")
    f.write(f"Total Words: {total_words}\n")
    f.write(f"Top {top_n} Words:\n")
    for word, count in word_count.most_common(top_n):
        f.write(f"{word} - {count}\n")
