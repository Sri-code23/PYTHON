# syntax for list comprehension
# [(expression) for (value) in (iterable) if (condition)]

"""
double=[]
for i in range(1,11):
    double.append(i*2)
print(double)
"""



"""
double=[i*2 for i in range(1,11)]
triple=[i*3 for i in range(1,11)]
square=[i*i for i in range(1,11)]

print(double)
print(triple)
print(square)
"""



"""
fruits=["apple","banana","orange"]
#          [(expression) for (value) in (iterable) 
upper_fruit=[fruit.upper() for fruit in fruits]
capital_fruit=[fruit.capitalize() for fruit in fruits]
first_letter=[fruit[0] for fruit in fruits]

print(upper_fruit)
print(capital_fruit)
print(first_letter)
"""



numbers=[1,-3,0,-9,5,+1]
pos_num=[num for num in numbers if num>=0]
neg_num=[num for num in numbers if num<=0]

print(pos_num)
print(neg_num)