"""
Exercise 11. Reverse a string using a for loop (no slicing)
Practice Problem: Write a program that takes a string and reverses it using a for loop. While Python’s [::-1] shortcut is famous, reversing a string manually is a classic way to understand how sequences are constructed.

Exercise Purpose: Learn how accumulation logic works. In Python, strings are “immutable,” which means you cannot change them directly. Here, you will practice building a new string by adding characters to the front. This is a key idea for algorithms that build results step by step.
"""

string ="Python"
length = len(string)
new_string = str()


# for char in range(length-1,-1,-1):
#     new_string += string[char]

# print(new_string)


for char in string:
  new_string = char + new_string

print(new_string)