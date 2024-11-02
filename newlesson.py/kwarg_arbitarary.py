def name(**kwarg):        # it stores the arguments in a dictionary
    #for key in kwarg.keys():
        #print(f"{key}")
    
    #for value in kwarg.values():
       #print(f"{value}")
    
    for key,value in kwarg.items(): 
        print(f"{key:10}:{value}")    

name(country="india",state="tn",city="hosur")        