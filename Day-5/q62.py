"""
Exercise 22. Print the alternate numbers pattern
Practice Problem: Write a program to print a pattern of alternate numbers from 1 to 20 (e.g., 1, 3, 5…).

Exercise Purpose: This exercise emphasises Step Logic in ranges. Being able to skip values efficiently without using unnecessary if statements inside your loop makes your code more “Pythonic” and faster to execute.

Given Input: Range: 1 to 20
"""

ranges = 20 

for i in range(1,ranges,2):
  print(i)