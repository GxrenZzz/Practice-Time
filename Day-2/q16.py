"""
Exercise 16. Numerical Palindrome Check

Practice Problem: Write a program to check if a given number is a palindrome (reads the same forwards and backwards).

Exercise Purpose: This exercise introduces the idea of “Reversing Logic.” Reversing a string is simple, but reversing an integer takes some math, like using division and modulo, or changing its type. This shows how data types can work differently.

"""

def check_palindrome(num:int) -> str:
  # print("original number", num)
  num_to_string = str(num)
  reversed_string = num_to_string[::-1]

  if num_to_string == reversed_string:
    print(f"{num_to_string} is a Palindrome ")
  else:
    print(f"{num_to_string} is not a Palindrome")

check_palindrome(121)
check_palindrome(125)