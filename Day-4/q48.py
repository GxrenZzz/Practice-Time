"""
Exercise 8. Count occurrences of a specific element in a list
Practice Problem: Given a list of numbers, use a loop to count how many times a specific number (e.g., 10) appears.

Exercise Purpose: This introduces Frequency Counting, a staple of data analysis. It shows how to iterate through a collection and use a conditional filter to increment a tally only when a match is found.
"""

list1 = [10, 20, 10, 30, 10, 40, 50]
target = 10
count = 0

for i in list1:
  if i == target:
    count += 1


print(f"{target} appear {count} times")