
try:   
    number=input("enter a number:")
    print(number/0)
except ZeroDivisionError:
    print("number cannot be divided")
except Exception as a:
    print("it seems something went wrong",a)

finally:
    print("code is runned")