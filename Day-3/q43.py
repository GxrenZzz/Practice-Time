"""
Exercise 3. Display a message “Done” after successful execution of for loop
Practice Problem: Write a program to display a message “Done” after the successful execution of a for loop that iterates from 0 to 4.

Exercise Purpose: This introduces a unique Python feature: the Loop-Else Clause. Unlike if-else, a loop else block only executes if the loop completes all its iterations without being interrupted by a break statement. This is useful for search loops to signal that a target was not found.
"""

for i in range(0,5):
  print(i)
else:
  print("Done")