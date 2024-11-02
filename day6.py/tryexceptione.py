try:
    a=int(input())
    b=int(input())#if you type somehing instead of numbers
    print(a+b) 
except Exception as e:
    print("something",e)