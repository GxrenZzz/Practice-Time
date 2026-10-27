"""
Exercise 33. Word frequency counter
Practice Problem: Write a program to count the frequency of each word in a given string.

Exercise Purpose: This introduces Mapping Logic. You learn to transform a “flat” string into a structured dictionary. This is the starting point for almost all Natural Language Processing (NLP) tasks, such as building a search engine or a tag cloud.

Given Input: text = "apple banana apple orange banana apple"
"""
text = "apple banana apple orange banana apple"
list_text = text.split()

word_count={}
for char in list_text:
  word_count[char] = word_count.get(char,0) + 1

print(word_count)
