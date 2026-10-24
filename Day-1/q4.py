"""
Exercise 4. String Slicing and Substring Removal
Practice Problem: Write a function to remove characters from a string starting from index 0 up to n and return a new string.

Exercise Purpose: This exercise demonstrates how to truncate data strings, a common data-cleaning task.
"""

def remove_chars(word:str,idx:int) -> str:
  idx_word = word[idx:]
  print(idx_word)


remove_chars("pynative", 4)
remove_chars("pynative", 2)


