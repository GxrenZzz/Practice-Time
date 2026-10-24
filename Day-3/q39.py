"""
Exercise 39. External File Word Counter
Practice Problem: Write a script that opens an existing .txt file and counts the total number of words it contains.

Exercise Purpose: This exercise teaches “Data Parsing.” In professional environments, you rarely work with data you typed into the code yourself; you almost always pull data from external sources. This script simulates basic text-mining techniques used to analyze documents or logs.
"""

with open("new_file.txt","r") as File:
  words = File.read()
  length = len(words.split())
  print(length)