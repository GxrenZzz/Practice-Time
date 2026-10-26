"""
Exercise 13. Count total number of digits in a number
Practice Problem: Write a program to count the total number of digits in a given integer using a while loop.

Exercise Purpose: This exercise introduces Arithmetic Reduction. Instead of treating the number as a string, you learn to peel off digits mathematically using floor division (//). This logic is common in algorithms involving digit manipulation, such as reversing numbers or checking for palindromes.

Given Input: 75869
"""
ins = 75869
count = 0
while ins != 0:
  ins = ins // 10
  count += 1

print(count)
