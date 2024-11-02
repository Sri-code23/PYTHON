def data(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    print()
    
    if "country" in kwargs:
        print(kwargs.get('country'))
    else:
        print(f"{kwargs.get('area')} ,{kwargs.get('no')} ,{kwargs.get('city')}")


    #for key,value in kwargs.items():
        #print(f"{key}:{value}")
data("sri","dharan","B",area="jj street", no=" 75/115",city="hosur")        