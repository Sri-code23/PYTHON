# Table of Content
- [1. Introduction to Python](#introduction-to-python)
- [2. Data Types](#data-types)
- [3. Data Structures](#data-structures)
- [4. Conditional Statements](#conditional-statements)
- [5. Loops](#loops)
- [6. Functions](#functions)
- [7. Modules](#modules)
- [8. File Handling](#file-handling)
- [9. Object-Oriented Programming](#object-oriented-programming)
- [10. Decorators](#decorators)
- [11. Magic Methods](#magic-methods)
- [12. Property Decorators](#property-decorators)
- [13. Special Functions](#special-functions)
- [14. String Operations](#string-operations)
- [15. Format Specifiers](#format-specifiers)
- [16. Conditional Expressions](#conditional-expressions)
- [17. List Comprehensions](#list-comprehensions)
- [18. Lambda Functions](#lambda-functions)
- [19. Match-Case](#match-case)

## Introduction to Python
Python is a high-level, interpreted programming language that is easy to learn and understand.

## Data Types
Python has several built-in data types:
- Integers: `int`
- Floating Point Numbers: `float`
- Strings: `str`
- Boolean: `bool`
- List: `list`
- Tuple: `tuple`
- Set: `set`
- Dictionary: `dict`

Example:
```python
# Integer
x = 5
print(type(x))  # Output: <class 'int'>

# Floating Point Number
y = 3.14
print(type(y))  # Output: <class 'float'>

# String
name = "John"
print(type(name))  # Output: <class 'str'>
```

## Data Structures
### Lists
A list is a collection of items that can be of any data type, including strings, integers, floats, and other lists.

Example:
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple
```

### Tuples
A tuple is a collection of items that can be of any data type, including strings, integers, floats, and other tuples.

Example:
```python
colors = ("red", "green", "blue")
print(colors[0])  # Output: red
```

### Sets
A set is an unordered collection of unique items.

Example:
```python
numbers = {1, 2, 3, 4, 5}
print(numbers)  # Output: {1, 2, 3, 4, 5}
```

### Dictionaries
A dictionary is an unordered collection of key-value pairs.

Example:
```python
person = {"name": "John", "age": 30}
print(person["name"])  # Output: John
```

## Conditional Statements
Conditional statements are used to execute different blocks of code based on certain conditions.

Example:
```python
x = 5
if x > 10:
    print("x is greater than 10")
else:
    print("x is less than or equal to 10")
```

## Loops
Loops are used to execute a block of code repeatedly.

### For Loop
Example:
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### While Loop
Example:
```python
x = 0
while x < 5:
    print(x)
    x += 1
```

## Functions
Functions are blocks of code that can be called multiple times from different parts of a program.

Example:
```python
def greet(name):
    print("Hello, " + name + "!")

greet("John")
```

## Modules
Modules are pre-written code that can be imported into a program.

Example:
```python
import math
print(math.pi)
```

## File Handling
File handling is used to read and write files.

Example:
```python
file = open("example.txt", "w")
file.write("Hello, World!")
file.close()
```

## Object-Oriented Programming
Object-oriented programming is a programming paradigm that uses objects and classes to organize code.

Example:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name + " and I am " + str(self.age) + " years old.")

person = Person("John", 30)
person.greet()
```

## Decorators
Decorators are used to modify the behavior of a function.

Example:
```python
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
```

## Magic Methods
Magic methods are special methods in Python classes that are surrounded by double underscores.

Example:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Name: " + self.name + ", Age: " + str(self.age)

person = Person("John", 30)
print(person)
```

## Property Decorators
Property decorators are used to implement getters and setters for class attributes.

Example:
```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

person = Person("John", 30)
print(person.name)
person.name = "Jane"
print(person.name)
```

## Special Functions
Special functions are built-in functions in Python that can be used to perform various tasks.

Example:
```python
print(dir())  # prints a list of all variables and functions in the current scope
print(help(len))  # prints the documentation for the len function
```

## String Operations
String operations are used to manipulate strings.

Example:
```python
name = "John"
print(name.upper())  # Output: JOHN
print(name.lower())  # Output: john
```

## Format Specifiers
Format specifiers are used to format strings.

Example:
```python
name = "John"
age = 30
print("My name is %s and I am %d years old." % (name, age))
```

## Conditional Expressions
Conditional expressions are used to evaluate a condition and return a value.

Example:
```python
x = 5
y = "x is greater than 10" if x > 10 else "x is less than or equal to 10"
print(y)
```

## List Comprehensions
List comprehensions are used to create lists in a concise way.

Example:
```python
numbers = [x for x in range(10) if x % 2 == 0]
print(numbers)
```

## Lambda Functions
Lambda functions are small anonymous functions.

Example:
```python
sum = lambda x, y: x + y
print(sum(5, 3))
```

## Match-Case
Match-case is a new feature in Python 3.10 that allows you to match values against patterns.

Example:
```python
def greet(language):
    match language:
        case "English":
            return "Hello!"
        case "Spanish":
            return "Hola!"
        case "French":
            return "Bonjour!"
        case _:
            return "I don't speak that language."

print(greet("English"))  # Output: Hello!
```