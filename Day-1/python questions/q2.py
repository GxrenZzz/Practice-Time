"""
Practice Problem: Iterate through the first 10 numbers (0-9). In each iteration, print the current number, the previous number, and their sum.

Exercise Purpose: This exercise teaches “State Tracking.” In programming, you often need to remember a value from a previous loop iteration to calculate results in the current one. This is the basis for algorithms like Fibonacci sequences or running totals.

"""

def sum_with_previous_num(r:int) -> str :
  previous_num = 0
  for i in range(r):
    sum_x = previous_num + i 
    print(f"Current Numeber : {i} , Previous Number : {previous_num} , Sum:{sum_x}")
    previous_num = i

ranges = int(input("Enter a Number : "))
sum_with_previous_num(ranges)