"""
def day_finder(day):
    if day==1:
        return "monday"
    elif day==2:
        return "tuesday"
    elif day==3:
        return "wednesday"
    elif day==4:
        return "thursday"
    elif day==5:
        return "friday"
    elif day==6:
        return "saturday"
    elif day==7:
        return "sunday"
    else:
        return "invalid input"
day=int(input("enter the number"))    
print(day_finder(day))
"""    
# to replace this code without using many elif (s)
# we can use match_case statement method

def day_finder(day):
    match day:    
        case 1:
            return "monday"
        case "tuesday" | "sunday":       #using string and using '|' as or condition 

            return True
        case 3:
            return "wednesday"
        case 4:
            return "thursday"
        case 5:
            return "friday"
        case 6:
            return "saturday"
        case 7:
            return "sunday"
        case _:                    # case _ to replace (else:)
            return "invalid input"
day=input("enter the number")    
print(day_finder(day))