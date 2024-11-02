#Count Divisors of a Number: Count how many numbers 
# between 1 and 20 are divisors of the number 12.
twl=0
for i in range(1,21):
    if(i%12==0):
        twl=twl+1
print("no of divisbles:",twl)