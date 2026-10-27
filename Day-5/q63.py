"""
Exercise 23. Print Alphabet pyramid (A, BB, CCC) pattern
Practice Problem: Write a program to print a triangle pattern where each row consists of the same letter, and the letter changes (increments) with each new row.

Exercise Purpose: This exercise introduces ASCII Value Manipulation. You’ll learn to use the chr() function to convert numbers into characters, so you can generate the alphabet dynamically without hardcoding each letter.
"""


rows = int(input("Enter a Number"))

for i in range(0,rows):
  for j in range(i+1):
    print(chr(65+i),end = " ")
  print()
