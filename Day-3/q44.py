"""
Exercise 4. Calculate the sum of all numbers from 1 to N
Practice Problem: Write a program that accepts a number from the user and calculates the sum of all numbers from 1 up to that number.

Exercise Purpose: This exercise teaches Value Accumulation. It shows how to use a loop to process data and store a running total in a variable, a common task in data processing.
"""

def sum(num):
  count = 0 
  for i in range(num+1):
    count += i

  return count


a = sum(10)
print(a)