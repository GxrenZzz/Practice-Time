"""
Exercise 20. Print right-angled triangle Number Pattern using a Loop
Practice Problem: Write a program to print a right-angled triangle pattern where each row contains increasing numbers up to the row number.

Exercise Purpose: This exercise introduces Nested Loops. It demonstrates how an “outer” loop can control the rows of a structure, while an “inner” loop handles the specific data printed within each row.

Given Input: None (Pattern height is 5).
"""

num = int(input("Enter a Number : "))

for i in range(1,num+1):
  for j in range(1,i+1):
    print(j, end=" ")
  print()