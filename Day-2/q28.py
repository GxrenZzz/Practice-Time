""" 
Exercise 28. Odd/Even List Splitter
Practice Problem: Start with a list of 10 numbers. Iterate through them and sort them into two separate lists: one for even numbers and one for odd numbers.

Given Input: numbers = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]
"""

def odd_even(list1:list) -> list[int]:
  odd = []
  even = [] 


  for i in list1:
    if i % 2 != 0:
      odd.append(i)
    else:
      even.append(i)

  return odd , even


a , b = odd_even([12, 7, 34, 21, 5, 10, 8, 3, 19, 2])


print(f"Even Numbers : {b}")
print(f"Odd Numbers : {a}")

