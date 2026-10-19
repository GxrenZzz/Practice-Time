"""
Exercise 1. Arithmetic Product and Conditional Logic

Practice Problem: Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.
"""

# Solution 


def mul_or_sum(num1,num2):

  prod = num1 * num2

  if prod <= 1000:
    return prod
  else:
    return num1 + num2

# Testing Case 1
result = mul_or_sum(20, 30)
print("The result is", result)

# Testing Case 2
result = mul_or_sum(40, 30)
print("The result is", result)