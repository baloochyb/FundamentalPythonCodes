import random as rnd

# This is a Python comment
answer = rnd.randint(1, 8)
"""This is a multiline comment in Python
This type of comment is sometimes called a docstring.
A docstring starts with three double-quotation marks, and also ends with three
double quotation marks. """
# This variable contains a string
txt1 = "Mary's dog said Woof"
txt2 = 'The dog of Mary said "Woof".'
# To escape a character, just precede it with a backslash (\).
txt3 = 'Mary\'s dog said "Woof".'
# (\n) to add a line break on the screen
print(txt1, "\n", txt2, "\n", txt3, "\n", "The old pond\nA frog jumped in,\nKerplunk!")
# This variable contains an integer
quantity = 10
# This variable contains a float
unit_price = 1.99
# This variable contains the result of multiplying quantity times unit price
extended_price = quantity * unit_price
# Show the results
print(extended_price)
