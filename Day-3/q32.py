"""
Exercise 32. Dictionary of Squares (Mapping Logic)
Practice Problem: Create a dictionary where the keys are numbers from 1 to 10 and the values are the squares of those numbers (e.g., 2: 4, 3: 9).

Exercise Purpose: This exercise explores “Data Mapping.” It demonstrates how dictionaries can be used to store pre-calculated mathematical relationships, essentially acting as a “lookup table” that can replace expensive repetitive calculations.
"""



def dict_mapping(x):
  dict1 = {}
  for i in range(1,x+1):
    dict1[i] = i ** 2

  return dict1


a = dict_mapping(10)
print(a)



