def some_function():
    print('This function can be used in other modules.')

if __name__ == '__main__':
    print("This will only be executed if this script is run directly.")
    some_function()
#If you run this script directly, both print statements will execute.
#If you import this script into another Python file,
#only some_function() will be available, and 
# the print("This will only be executed...") statement won't run

