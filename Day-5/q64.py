"""
Exercise 24. Hollow square pattern
Practice Problem: Print a 5*5 square of stars where the middle is empty, leaving only the border.

Exercise Purpose: This exercise teaches Boundary Condition Logic. Instead of printing every item in a nested loop, you use if statements to identify edges, such as the first or last rows and columns, which is essential for UI layouts and 2D array processing.
"""


nums = int(input("Enter a number "))

for i in range(nums):
  for j in range(nums):
    if i == 0 or i == nums - 1 or j == 0 or j == nums - 1:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()

