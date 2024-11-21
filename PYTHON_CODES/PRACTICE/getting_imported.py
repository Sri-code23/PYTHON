from calendar import isleap

class Leap_Year:
    def leap_year(year):
        if isleap(year) is True:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
        print("thank for using this module")     