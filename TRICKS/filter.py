# Explanation of filter()
# ======================

# The filter() function in Python is a built-in function that takes a function and a sequence (such as a list, tuple, or string) as input, 
# and returns a new sequence that includes only the items for which the function returns True.

# Definition of filter()
# ======================

# filter(function, sequence)

# Syntax of filter()
# ===================

# filter(lambda x: x > 5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Example Usage of filter()
# ==========================

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def is_even(num):
    return num % 2 == 0

even_numbers = list(filter(is_even, numbers)) 
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# Using lambda function with filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]