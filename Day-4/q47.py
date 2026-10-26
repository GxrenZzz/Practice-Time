"""
Exercise 7. Display numbers from a list using a loop
Practice Problem: Given a list of numbers, iterate through it and print numbers that satisfy these conditions:

The number must be divisible by five.
If the number is greater than 150, skip it and move to the next.
If the number is greater than 500, stop the loop entirely.
Exercise Purpose: This vital Flow Control exercise introduces continue (to skip) and break (to exit), essential for writing efficient code that avoids processing unnecessary data.

"""

numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
  if i % 5 == 0:
    if i > 500:
      break
    elif i > 150:
      continue 
    else:
      print(i)
