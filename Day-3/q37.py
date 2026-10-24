"""
Exercise 37. Simple Countdown Timer
Practice Problem: Create a countdown timer that starts from a given number and counts down to zero using a while loop.

Exercise Purpose: In this exercise, you will learn about loop termination logic and time delay management. Knowing how to control the flow of your code in real time is important for making animations, game loops, or automated scripts.

Given Input: start_count = 5

Expected Output: 5 4 3 2 1 Blast off!
"""

import time

i = int(input("Enter a number "))

while i > 0:
  print(i)

  time.sleep(2)

  i -= 1

print("Blast Off")