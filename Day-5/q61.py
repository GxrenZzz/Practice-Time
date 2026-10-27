"""
Exercise 21. Print the decreasing pattern
Practice Problem: Write a program to use for loop to print the following reverse number pattern:

5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1

Exercise Purpose: This exercise builds on nested loops and introduces Dynamic Range Boundaries. It shows how to make the inner loop’s starting point depend on the outer loop’s current value to create decreasing structures.
"""

n = int(input("Enter A Number :  "))

for i in range(n,0,-1):
  for j in range(i,0,-1):
    print(j,end=" ")
  print()