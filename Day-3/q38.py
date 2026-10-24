"""
Exercise 38. File Creation and Basic I/O
Practice Problem: Write a program that creates a new text file named notes.txt, writes three separate lines of text to it, and then reads that file back to display the contents in the console.

Exercise Purpose: This exercise introduces “Persistent Storage.” Unlike variables that disappear when the program stops, files allow you to save data to the hard drive. Learning the open(), write(), and read() workflow is essential for building logging systems and saving user settings.
"""

with open("new_file.txt","w") as File:
  File.write("Hello, this is my first note.\n")
  File.write("Python file handling is simple.\n")
  File.write("End of file.\n")

with open("new_file.txt","r") as File:
  print(File.read()) 