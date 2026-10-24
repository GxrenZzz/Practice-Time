"""
Exercise 40. Introduction to Classes (OOP)
Practice Problem: Create a Car class with attributes for make, model, and year. Include a method called start_engine() that prints a formatted string describing the car starting up.

Exercise Purpose: This exercise introduces Object-Oriented Programming (OOP). Instead of just writing functions, you are creating a “Blueprint” (the Class) to generate “Objects” (the specific cars). This is how modern software is built, allowing you to organize code into logical, reusable components.
"""

class Car:
  def __init__(self,make,model,year):
    self.make = make
    self.model = model
    self.year = year

  def start_engine(self):
    print(f"The {self.year} {self.make} {self.model} Engine's now Running")


obj1 = Car("BMW","M4 Comp",2022)
obj1.start_engine()