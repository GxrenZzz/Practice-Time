"""
Exercise 5. Variable Swapping (The In-Place Method)
Practice Problem: Write a program to swap the values of two variables, a and b, without using a third temporary variable.

Exercise Purpose: This exercise will help you learn about memory efficiency and Python’s special tuple unpacking feature. In other languages like C or Java, you need a temporary variable to swap values safely. In Python, you can swap values in one line without risking data loss.
"""


a , b = 5,10

a , b = b , a

print(a)
print(b)