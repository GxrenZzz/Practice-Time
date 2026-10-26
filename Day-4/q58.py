"""
Exercise 18. Collatz Conjecture: Generate a sequence until it reaches 1
Practice Problem: The Collatz conjecture states that if you start with any positive integer n, and if n is even, divide it by 2; if n is odd, multiply it by 3 and add 1. Repeat the process. The sequence will always eventually reach 1. Write a program to print this sequence for a given number.

Exercise Purpose: This exercise demonstrates Indeterminate Iteration. Unlike a for loop with a known range, a while loop runs until a specific mathematical condition, reaching 1, is met.
"""

inputs = int(input("Enter a Number : "))
while inputs != 1:
  print(inputs,end=" ")
  if inputs % 2 == 0:
    inputs = inputs // 2
  else:
    inputs = (inputs * 3) + 1