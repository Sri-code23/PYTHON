#value error
try:
    a=int(input())
    b=int(input())#if you type somehing instead of numbers
    print(a/b)
except ValueError as e:
    print("value error",e)