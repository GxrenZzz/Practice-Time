"""
Exercise 34. Display fibonacci series up to 10 terms
Practice Problem: Write a program to display the Fibonacci sequence up to 10 terms. The sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones.

Exercise Purpose: This exercise teaches State Management. You keep track of two changing variables (n1 and n2) and update them in sync to crawl forward through the sequence.
"""


a = 0
b = 1

for i in range(10):
  print(a, end=" ")
  a , b = b , a+b
