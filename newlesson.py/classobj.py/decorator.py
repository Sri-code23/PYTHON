def add_toppings(function_calling):
    def wrapper(*args):
        def decorat(*args):
            print("here is your ice cream with toppings")
            function_calling(*args)
            print("finished")
        return decorat
    return wrapper

@add_toppings("chocolate")
def ice_cream(flavor):
    print(f"here is your {flavor} ice cream")

ice_cream("vanilla")    