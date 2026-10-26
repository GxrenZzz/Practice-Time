"""
Exercise 15. Find largest and smallest digit in a number
Practice Problem: Write a program to find the largest and smallest digit within a given integer (e.g., in 75869, the largest is 9 and the smallest is 5).

Exercise Purpose: This combines Digit Extraction (from Exercise 14) with Min/Max Comparison. It’s a foundational logic for finding “extremes” in a dataset. You learn how to initialize comparison variables and update them dynamically as you scan through data.
"""
num = 75869
ins = abs(num)
largetst = 0 
smallest = 9
while ins > 0:
  digit = ins % 10 

  if digit > largetst:
    largetst = digit
  if digit < smallest :
    smallest = digit

  ins = ins // 10

print(largetst)
print(smallest)