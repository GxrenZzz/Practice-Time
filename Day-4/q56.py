"""
Exercise 16. Check if a number is a palindrome
Practice Problem: Write a program to check if a given number is a palindrome. A palindrome number is a number that remains the same when its digits are reversed (e.g., 121, 343).

Exercise Purpose: This exercise combines Mathematical Reversal with Conditional Comparison. It teaches storing an original value before modifying it in a loop so you can perform a final validation.

Given Input: number = 121
"""


num = 121 
target = num
rev= 0 

while num != 0:
  digit = num % 10
  rev = (rev*10) + digit
  num = num // 10 


if rev == target:
  print("Yes")
else:
  print("NO")
