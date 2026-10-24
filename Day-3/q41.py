""""
Exercise 41. Print first 10 natural numbers using while loop
Practice Problem: Write a program to print the first 10 natural numbers using a while loop. Each number should be printed on a new line.

Exercise Purpose: This is the fundamental introduction to iteration. It teaches how to set up a loop condition to execute a block of code repeatedly, and manually manage a counter variable to prevent infinite loops.
"""

num = int(input("Enter a Number "))

i = 1

while i <= num:
  print(i)
  i += 1
