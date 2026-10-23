""" 
Exercise 21. Downward Half-Pyramid Pattern

Practice Problem: Print a downward half-pyramid pattern using stars (*).

Exercise Purpose: Learn about reverse indexing. Controlling loop boundaries in reverse is important for algorithms that process data from end to beginning.
"""


num = int(input("Enter a Number "))

for i in range(0,num):
  for j in range(num-i):
    print("*",end=" ")
  print()