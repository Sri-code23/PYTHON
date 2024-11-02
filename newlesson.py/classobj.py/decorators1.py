# Define the decorator
def my_decorator(say_hello):
    def wrapper(name,friend):
        print(f"welcom {name} and {friend}")
        say_hello(name,friend)
        print(f"bye {name} and {friend}")
    return wrapper

# Use @ to apply the decorator
@my_decorator
def say_hello(name,friend):
    print(f"Hello {name}! and {friend}")

# Call the decorated function
say_hello("sri","friend")


"""
class User:
    def __init__(self):
        self.username = 'john'
        self.is_admin = False

user1 = User()  # Creating an instance of the class
"""

#user1 = type('User', (), {'username': 'john', 'is_admin': False})()

