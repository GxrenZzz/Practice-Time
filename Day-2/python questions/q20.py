"""
Exercise 20. Nested Loops for Multiplication Tables
Practice Problem: Print a multiplication table from 1 to 10 in a formatted grid.

Exercise Purpose: To master “Matrix Generation.” This builds on the nested loop concepts from Exercise 8 and applies them to generate a structured data table. This is essential for understanding how to populate 2D arrays or generate spreadsheets.

"""

num = int(input("Enter a Number "))

for i in range(1,num+1):
  for j in range(1,num+1):
    print(i*j,end="\t")
  print(" ")