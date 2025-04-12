# 1. Ask name and year of birth, tell age

name = input("Enter your name: ")
year = int(input("Enter your birth year: "))
age = 2025 - year
print(f"Hello {name}, you are {age} years old.")


# 2. Extract car names from 'LMaasleitbtui

txt = 'LMaasleitbtui'
car_name = txt[::2]
print("Extracted:", car_name)

# 3. String input - length, uppercase, lowercase

text = input("Enter a string: ")
print("Length:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())


# 4. Check if string is a palindrome

text = input("Enter a string: ")
if text == text[::-1]:
    print("Palindrome!")
else:
    print("Not a palindrome.")

# 5. Count vowels and consonants

text = input("Enter a string: ").lower()
vowels = "aeiou"
vowel_count = sum(1 for char in text if char in vowels)
consonant_count = sum(1 for char in text if char.isalpha() and char not in vowels)
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)

# 6. Check if one string contains another

text = input("Enter main string: ")
word = input("Enter word to find: ")
print(word in text)


# 7. Replace a word in sentence

sentence = input("Enter a sentence: ")
old = input("Word to replace: ")
new = input("New word: ")
print(sentence.replace(old, new))


# 8. Print first and last characters

text = input("Enter a string: ")
print("First character:", text[0])
print("Last character:", text[-1])

# 9. Print reversed string

text = input("Enter a string: ")
print("Reversed:", text[::-1])


# 10. Count words in a sentence

sentence = input("Enter a sentence: ")
words = sentence.split()
print("Number of words:", len(words))

# 11. Check if string has digits

text = input("Enter a string: ")
print(any(char.isdigit() for char in text))

# 12. Join list of words with separator

words = ["apple", "banana", "cherry"]
joined = "-".join(words)
print("Joined string:", joined)


# 13. Remove all spaces from string

text = input("Enter a string: ")
print("No spaces:", text.replace(" ", ""))

# 14. Check if two strings are equal

a = input("Enter first string: ")
b = input("Enter second string: ")
print("Equal?" , a == b)

# 15. Create acronym

sentence = input("Enter a sentence: ")
acronym = ''.join(word[0].upper() for word in sentence.split())
print("Acronym:", acronym)

# 16. Remove all occurrences of a character

text = input("Enter a string: ")
char = input("Character to remove: ")
print(text.replace(char, ""))

# 17. Replace vowels with symbol

text = input("Enter a string: ")
vowels = "aeiouAEIOU"
for v in vowels:
    text = text.replace(v, "*")
print(text)

# 18. Check start and end

text = input("Enter a sentence: ")
start = input("Starts with: ")
end = input("Ends with: ")
print(text.startswith(start) and text.endswith(end))

