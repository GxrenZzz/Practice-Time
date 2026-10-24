"""
Practice Problem: Write a program to check if a user-entered string contains any numeric digits. Use a for loop to examine each character.

Exercise Purpose: This exercise will help you learn about string traversal and character analysis. In software development, these skills are important for tasks like checking if a username has forbidden characters or if a password is complex enough.

Given Input: input_string = "Python3"

Expected Output: The string 'Python3' contains digits: True

"""


input_string = "Python3"
contains_digit = False

for char in input_string:
  if char.isdigit():
    contains_digit = True
    break

print(f"The string '{input_string}' contains digit : {contains_digit} ")

