# Map() Function in Python
# =========================
# The map() function applies a given function to each item of an iterable (such as a list, tuple, or string) and returns a list of the results.

# Syntax:
# -------
# map(function, iterable)

# Explanation:
# ------------
# The map() function takes two arguments: a function and an iterable. It applies the function to each item in the iterable and returns a new iterable with the results.

"""
square=lambda x,y :x**y
print(square(2,3)) # Output: 8
"""


# Using map() to convert strings to integers
strings = ['1', '2', '3', '4', '5']
integers = list(map(int, strings))
print(integers)  # Output: [1, 2, 3, 4, 5]

# Using map() to convert strings to uppercase
words = ['hello', 'world', 'python']
uppercase_words = map(str.upper, words)
print(list(uppercase_words))  # Output: ['HELLO', 'WORLD', 'PYTHON']
