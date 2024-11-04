def sum_decor(add):
    def value(a,b,ad):
        print(f"you performed {ad}")
        add(a,b)
        print("you finished")
    return value

@sum_decor
def add(a,b,ad=""):
    print(f" addition : {a+b}")
    
add(4,5,"addition")