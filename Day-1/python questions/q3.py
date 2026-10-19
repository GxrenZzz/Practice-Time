"""
Practice Problem: Display only those characters which are present at an even index number in given string.

Exercise Purpose: Understand how data is stored in memory using zero-based indexing. In most languages, 
the first character is at position 0, the second at 1, and so on. Mastering indexing is vital for data parsing.
"""

string = "pynative"

# through looping

# for i in range(len(string)):
#   if i%2==0:print(string[i])

# start:end:step

# for i in range(0,len(string)-1,2):
#   print(string[i])

# slicing

# even_Chars = string[::2]

# for chars in even_Chars:
#   print(chars)