#count both even and odd
even=0 #random variable (even) used to store even 
odd=0 #random variable (odd) used to store the odd
for i in range(0,11):
    if (i%2==0):
        even=even+1 #if (if) is satisfied the variable (even) is updated with +1
    else:
        odd=odd+1#if (else) is satisfied the variable (even) is updated with +1
print("even nos:",even)
print("odd nos:",odd)