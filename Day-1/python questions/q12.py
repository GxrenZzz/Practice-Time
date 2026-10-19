"""
Exercise 12. List Comparison and Boolean Logic
Practice Problem: Write a function to return True if the first and last number of a given list is the same. If the numbers are different, return False.

Exercise Purpose: This exercise introduces “Collection Indexing” and “Boolean Flags.” Comparing data structure boundaries is common in pattern matching and data integrity checks.
"""

from typing import *

def match_list(x:List) -> List:
  if x[0] == x[-1]:
    print("result is True")
  else:
    print("result is false")

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

match_list(numbers_x)
match_list(numbers_y)