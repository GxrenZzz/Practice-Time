"""
Exercise 14. Reverse an integer number
Practice Problem: Write a program to reverse a given integer number (e.g., 76542 should become 24567).

Exercise Purpose: While you could convert the number to a string and slice it, doing it mathematically is more efficient and teaches you to use Modulo (%) and Floor Division (//) together to manipulate digits.
"""

ins = abs(76542)
length  = len(str(abs(ins)))
i = 0 
rev_dig = 0 
if ins == 0:
    count = 1
while i < length:
    digit = ins %  10 
    rev_dig = (rev_dig * 10) + digit
    ins = ins // 10
    i += 1
print(rev_dig)