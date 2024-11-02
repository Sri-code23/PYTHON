def greet():
    print("Hello! This is the greet function.")

# This block will only run if the script is executed directly
if __name__ == '__main__':
    print("This script is being run directly.")
    greet()
else:
    print("This script has been imported.")
