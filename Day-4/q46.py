"""
Exercise 6. Calculate the cube of all numbers from 1 to a given number
Practice Problem: Write a program that takes an integer n and prints the cube of every number from 1 to n in the format Current Number is : 1 and the cube is 1.

Exercise Purpose: This exercise teaches Result Formatting and Power Operations. It shows how to combine text with calculated variables using f-strings or commas and perform exponentiation with the ** operator or pow() function.
"""

i  = int(input("Enter a Number : "))
for i in range(1,i+1):
  print(f"Current Number : {i} and the Cube is : {pow(i,3)}") # or i ** 3 anything works