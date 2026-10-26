"""
Exercise 19. Armstrong Number Check
Practice Problem: Write a program to check if a number is an Armstrong number. An Armstrong number (for a 3-digit number) is an integer such that the sum of the cubes of its digits is equal to the number itself (e.g., 153 = 1^3 + 5^3 + 3^3).

Exercise Purpose: This logic-heavy exercise combines Type Conversion, Mathematical Iteration, and Power Operations. It tests your ability to break a complex problem into steps: isolate digits, raise them to a power, and compare the sum.
"""

num = 121
str_num = str(num)
total = 0 

for i in str_num:
  total += int(i) ** 3

if total == num:
  print("Armstrong it is")
else:
  print("Not an Armstring")