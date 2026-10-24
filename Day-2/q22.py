"""
Practice Problem: Write a function called exponent(base, exp) that returns an integer value of the base raised to the power of the exponent.

Exercise Purpose: Learn about “Accumulator Patterns.” Although Python has a built-in power operator (**), making your own version shows how repeated multiplication works and how functions return results to the main program.
"""


def exponent(base:int ,exp):
   num = exp
   res = 1
   while  num > 0:
      res = res * base
      num -= 1

   print(f"{base} to the power of {exp} is : {res}")


exponent(2,5)