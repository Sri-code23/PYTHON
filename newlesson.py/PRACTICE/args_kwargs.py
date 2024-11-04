class args_kwargs:
    def add(*args):
        total=0
        for i in args:
            total=total+i
        print(f"Total : {total}")    
    

    def name_list(**kwargs):
        for keys,values in kwargs.items():
            print(f" {keys} // {values}")
        print(f" Name_List: {kwargs}")

if __name__=="__main__":
    obj1=args_kwargs.add(1,2,3,4,5)
    print("---------------")
    args_kwargs.name_list(name="dharan",age=20)
