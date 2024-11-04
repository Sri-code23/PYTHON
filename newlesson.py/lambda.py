# Lambda function explanation
# A lambda function is a small anonymous function in Python.
# It can take any number of arguments, but can only have one expression.

# Example of a lambda function
# This lambda function takes one argument 'x' and returns its square
sum = lambda x, y: x + y
print(sum(3, 4))

# Example of a lambda function with a list comprehension
numbers = [1, 2, 3, 4, 5]

# Using a lambda function with list comprehension to create a new list
squares = [num ** 2 for num in numbers]
print(squares)
#output : [1, 4, 9, 16, 25]

list2=[numbers]
#print(list2) 
# Output : [[1, 2, 3, 4, 5]]




# Example of a lambda function with a dictionary comprehension
dictionary = {'a': 1, 'b': 2, 'c': 3}

# Using a lambda function with dictionary comprehension to create a new dictionary
squares_dict = {key: value ** 2 for key, value in dictionary.items()}
print(squares_dict)
#output : {'a': 1, 'b': 4, 'c': 9}


temp=0
print(f"{"high" if temp>1 else "low"}") 
#method name:  conditional expression

#output : low

multi=lambda a,b,c:a*b*c
print(f"{multi(1,2,1)}")
#output:  2
