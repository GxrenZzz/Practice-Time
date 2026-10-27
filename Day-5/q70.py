"""
Exercise 30. Remove duplicates without set
Practice Problem: Write a program to remove all duplicate values from a list using a loop, maintaining the original order of elements.

Exercise Purpose: Although set(list) quickly removes duplicates, it destroys order. This exercise teaches Uniqueness Validation, ensuring each piece of data is processed once while preserving sequence.
"""

x = [1, 2, 2, 3, 4, 4, 4, 5]
y =[]
for i in x:
  if i not in y:
    y.append(i)

print(y)