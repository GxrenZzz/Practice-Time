"""
Exercise 31. Even/Odd Segregation: Move evens to front, odds to back
Practice Problem: Given a list of integers, move all even numbers to the beginning of the list and all odd numbers to the end.

Exercise Purpose: This introduces List Reorganization, a simplified version of the partitioning logic used in QuickSort algorithms. You learn to categorize data and reassemble it into a specific structural order.


"""

x = [1, 2, 3, 4, 5, 6]

odds = []
evens =[]

for i in x:
  if i % 2 ==0:
    evens.append(i)
  else:
    odds.append(i)

combine_list = evens + odds
print(combine_list)