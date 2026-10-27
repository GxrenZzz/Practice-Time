""" 
Exercise 35. Perfect number check
Practice Problem: Write a program to check if a number is a “Perfect Number.” A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding the number itself). For example, 6 is perfect because 1 + 2 + 3 = 6.

Exercise Purpose: Emphasizes efficiency in search. While you could check every number up to n, you only need to check up to n/2 to find all divisors, showing how to optimize loop ranges.
"""


nums = int(input("Enter a Number "))
divisor_sum = 0 

for i in range(1,nums//2 +1 ):
  if nums % i == 0:
    divisor_sum += i

if divisor_sum == nums:
  print("Turururuururu")
else:
  print("Falalalalallse")
