"""
Exercise 26. Print full multiplication table (1 to 10)
Practice Problem: Write a program to print the full multiplication table from 1 to 10 in a grid format.

Exercise Purpose: This is the ultimate test for Tabular Data Representation. It forces you to think about how nested loops interact. The outer loop represents the rows (multiplicands), and the inner loop represents the columns (multipliers). It also introduces the use of escape characters like \t (tab) to align text columns perfectly.
"""

nums = 10 
for i in range(1,nums+1):
  for j in range(1,nums+1):
    print((i*j) ,end="\t")
  print()