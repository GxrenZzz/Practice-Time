"""
Exercise 4. Print multiplication table of a given number
Practice Problem: Create a program that takes an integer and prints its multiplication table from 1 to 10.

Exercise Purpose: This reinforces the use of loops for generating Mathematical Sequences. It shows how to use the loop index (i) as a multiplier against a fixed constant.

"""

def multiple(num:int,ranges:int):
  for i in range(1,ranges+1):
    res = num * i
    print(res)

a = multiple(1021,10)