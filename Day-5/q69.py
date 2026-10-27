"""
Exercise 29. Find common elements (Intersection) using loop
Practice Problem: Given two lists, find the elements that appear in both. Do not use Python’s built-in set().intersection() method.

Exercise Purpose: This exercise focuses on Cross-Reference Iteration. It demonstrates how to use one collection as a master list and check its members against a secondary “filter” list to find commonalities.
"""

list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
common  = []

for x in list_a:
  if x in list_b:
    common.append(x)

print(common)