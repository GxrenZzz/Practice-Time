"""
Exercise 19. Multi-Tiered Income Tax Calculation

Practice Problem: Calculate income tax for a given income based on these rules:

First $10,000: 0% tax
Next $10,000: 10% tax
Remaining income: 20% tax

Exercise Purpose: This exercise introduces “Tax Brackets” logic, a classic example of complex conditional branching. It shows how to calculate values cumulatively instead of applying a single percentage to the entire amount.
"""


def tax_bracket(num:int) -> str:
  tax_payable = 0

  if num <= 10000:
    tax_payable = 0 
  elif num <= 20000:
    tax_payable += (20000-10000) * 10/100
  else:
    # first 10000
    tax_payable = (10000 * 10/100)
    tax_payable += (num-20000) * 20 / 100 

  return tax_payable


print(tax_bracket(45000))

    

