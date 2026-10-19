"""
Practice Problem: Write a program to count the total number of vowels (a, e, i, o, u) present in a given sentence.

Exercise Purpose: This exercise introduces “Membership Testing.” By checking if a character belongs to a specific group (the vowels), you learn how to filter data based on categories. This is a fundamental step toward building text-analysis tools or spam filters.
"""

sentence = "Learning Python is fun!"

string = "aeiou"

vowel_count = 0

for char in sentence.lower():
  if char in string:
    vowel_count += 1

print(vowel_count) 

