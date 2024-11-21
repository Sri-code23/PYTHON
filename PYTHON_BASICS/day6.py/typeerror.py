#type error
try:
    a=int(input())
    b=int(input())#if you type somehing instead of numbers
    print(a/b)
except Typeerror as e:
    print("type error",e)