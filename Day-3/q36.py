"""
Practice Problem: Write a program to capitalize the first letter of each word in a given string without using the built-in .title() method.

Exercise Purpose: In this exercise, you will learn about “Tokenization” and “String Re-assembly.” You will split a sentence into words, change them, and then put the sentence back together. This helps you practice working with complex data structures.

Given Input: text = "hello world from python"

Expected Output: Hello World From Python
"""


def capitalize(sentence:str) -> str:
  sentence_words = sentence.split()
  new_list = []
  for i in sentence_words:
      capital = i[0].upper() + i[1:]
      new_list.append(capital)
  list_to_string = " ".join(new_list)
  return list_to_string
    



a = capitalize("hello world from python")
print(a)