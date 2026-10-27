"""
Exercise 28. Dictionary Filter: Extract pairs where value exceeds a threshold.
Practice Problem: Given a dictionary of student scores, create a new dictionary that only includes students who scored above a certain threshold (e.g., 75).

Exercise Purpose: This exercise teaches Dictionary Iteration. Unlike lists, dictionaries have keys and values. You learn to use .items() to unpack both at once and how to conditionally build a new mapping.
"""

scores = {"Alice": 85, "Bob": 70, "Charlie": 95, "David": 60}
threshold = 75
passing_student ={name:value for name,value in scores.items() if value > threshold}

print(passing_student)