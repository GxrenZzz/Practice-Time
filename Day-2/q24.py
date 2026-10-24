"""
Exercise 24. Generate Fibonacci Series
Practice Problem: Write a program to print the first 15 terms of the Fibonacci series. The sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones.

Exercise Purpose: The Fibonacci sequence is a classic way to learn about state management in loops. You keep track of two changing variables at once to find the next number, which helps you see how data moves through each step.
"""


def fibonaaci(num:int):
  a = 0
  b = 1
  for i in range(num):
    print(a , end=" ")
    a,b = b , a + b


fibonaaci(15)