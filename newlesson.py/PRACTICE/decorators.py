def decoration_function(greeting):
    def decoration2(pronoun,name : str):   
        print("1 --------------")
        greeting(name)
        print("2 --------------")
        print("3 --------------")
        return f"Hello, {pronoun}.{name}"
    return decoration2




@decoration_function
def greeting(name):      #this function is accessed or called only in the 4 line
    print(f" welcome {name} !")

greeting("Mr","sri")






# Example usage of a decorator
"""
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.

"""
"""
def my_decorator(func):
    # This is a decorator function that takes another function as an argument
    def wrapper():
        # This is a nested function inside the decorator function
        print("Something is happening before the function is called.")
        # The decorator function calls the original function
        func()
        print("Something is happening after the function is called.")
    # The decorator function returns the wrapper function
    return wrapper

# This is an example of a function that will be decorated
@my_decorator
def say_hello():
    # This is the original function that will be decorated
    print("Hello!")

# This is how you call the decorated function
say_hello()

# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.

"""