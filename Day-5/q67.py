"""
Exercise 27. List Cumulative Sum: Each element is the sum of all previous
Practice Problem: Given a list of numbers, create a new list where each element is the sum of all elements from the original list up to that position.

Exercise Purpose: This introduces the Running Total pattern. It is essentially “memory” within a loop, carrying the result of previous iterations into the current one. This logic is used in financial ledgers to calculate a balance after each transaction.
"""

nums = [1, 2, 3, 4]
total = 0
cul_nums = []
for i in range(1,len(nums)+1):
  total+= i
  cul_nums.append(total)

print(cul_nums)