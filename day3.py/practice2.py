#Count Positive and Negative Numbers: Count the number of
#  positive and negative numbers in the range from -5 to 5.
pos=0
neg=0
for i in range(-2,3):
    if (i==-i):
        neg+=1
    else:
        pos+=1
print("poitive;",pos)
print("negative:",neg)