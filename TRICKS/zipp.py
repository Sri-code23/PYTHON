# Using zip() with lists of different lengths
a = [1, 2, 3]
b = ['a', 'b', 'c', 'd' , 'e' ,'f','g']

c = zip(a, b,range(1,5))
for roll,inita,size in c:
    print(f"Roll: {roll}, Initials: {inita}, size: {size}" )

