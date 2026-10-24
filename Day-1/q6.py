"""
Exercise 6. Calculating Factorial with a Loop
Practice Problem: Write a program that calculates the factorial of a given number (e.g., 5!) using a for loop.

Exercise Purpose: This exercise explores “Mathematical Accumulation.” A factorial (e.g., 5! = 5*4*3*2*1) requires you to maintain a running product across multiple iterations, which is a core pattern in scientific computing.
"""


def factorial(num:int) -> int :
  fact = 1
  for i in range(1,num+1):
    fact = fact * i 

  return fact
 
num = int(input("Enter a Number : "))
print(f"The Factorial of {num} is : {factorial(num)}") 