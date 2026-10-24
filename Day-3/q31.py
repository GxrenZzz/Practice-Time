"""
Exercise 31. Print Alternate Prime Numbers
Practice Problem: Write a program to find all prime numbers up to 20, but only print every second (alternate) prime number found.

Exercise Purpose: This exercise combines “Nested Loops” (to check for primality) with “Step Logic.” It requires the programmer to first identify a subset of data and then apply a secondary filter, a common task in data reporting. 
"""

# a = [2,3,5,7,11,13,17]


def alternate(number:int) -> list:
  alternate_primes = [] 
  for num in range(2,number):
    for divisor in range(2,int(num ** 0.5) + 1): 
      # used root to reduce the number of Divisibilty Checks
      if num % divisor == 0:
        break
    else:
      alternate_primes.append(num)

  return alternate_primes[::2]

a = alternate(21)
print(a)