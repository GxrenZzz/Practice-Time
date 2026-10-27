"""
Exercise 25. Print pyramid pattern of stars
Practice Problem: Write a program to print the following pattern using nested loops:

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
Exercise Purpose: Introduce Symmetrical Logic. It combines an increasing and a decreasing pattern. You learn to use two separate loop structures sequentially to create a complex visual shape.
"""

nums = 5 

for i in range(1,nums+1):
  for j in range(i):
    print("*",end=" ")
  print("\r")

for i in range(nums,1,-1):
  for j in range(i-1):
    print("*",end=" ")
  print()