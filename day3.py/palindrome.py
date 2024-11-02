#Iterate through all 3-digit numbers from 100 to 999.
#Check if each number is a palindrome.
#Count how many such numbers exist in the given range.
count=0
for i in range(100,999): # if 101 is input 
    a=i//100 #a=1
    c=i%10 #c=1
    if a==c: #true
        count=count+1 #count=0+1=1
print("count:",count)