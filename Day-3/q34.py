"""
Exercise 34. Print Reverse Number Pattern
Practice Problem: Print a downward number pattern where each row starts with a decreasing value.

Exercise Purpose: In this exercise, you will learn about range control and practice using negative steps in loops to move backwards. This skill is important for algorithms that process data from the end of a file to the beginning.
"""


n = int(input("Enter a Number : "))
for i in range(n):
  for j in range(n-i,0,-1):
    print(j,end=" ")
  print()