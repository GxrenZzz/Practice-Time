"""
Exercise 17. Find factorial of a number
Practice Problem: Write a program to use a loop to find the factorial of a given number (e.g., 5!). The factorial of N is the product of all integers from 1 to N.

Exercise Purpose: Factorials grow fast. This exercise demonstrates Iterative Multiplication, a core concept used in probability, statistics, and combinatorics.

Given Input: num = 5

Expected Output: 120
"""

num = int(input("Enter A number"))
res = 1
for i in range(1,num+1):
  res = res * i 

  

 
print(res)