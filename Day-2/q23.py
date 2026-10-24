"""
Exercise 23. Check Palindrome Number

Practice Problem: Write a program to check if a given number is a palindrome. A palindrome number remains the same when its digits are reversed (e.g., 121, 545).

Exercise Purpose: This exercise teaches “Algorithmic Reversal.” While strings are easy to reverse in Python, reversing a number mathematically using the modulo (%) and floor division (//) operators deepens understanding of how integers are stored in memory and how to manipulate digits individually.
"""

def palindrome(num:int) -> bool:

    num_to_str = str(num)
    reversed_string = num_to_str[::-1]

    return True if num_to_str == reversed_string else False


num = int(input("Enter a Number")) 

if palindrome(num):
    print(f"Yes {num} is a Palindrome")
else:
    print(f"No {num} is not a Palindrome")
   