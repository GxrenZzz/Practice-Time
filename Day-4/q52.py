"""
Exercise 12. Count vowels and consonants in a sentence
Practice Problem: Write a program that counts the total number of vowels and consonants in a given sentence, ignoring spaces and special characters.

Exercise Purpose: In this exercise, you will practice membership testing and data filtering. You will use the in operator to check if a value is in a collection, and try string methods like .isalpha() to quickly clean your data.
"""

sentence = "Loops are Fun!"
vowels = "aeiou"
v_count = 0
c_count = 0

for char in sentence.lower():
    if char.isalpha():  # Only process letters
        if char in vowels:
            v_count += 1
        else:
            c_count += 1

print(f"Vowels: {v_count}")
print(f"Consonants: {c_count}")