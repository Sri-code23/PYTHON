import random
a=1
b=5
cards=["1","2","3","4","5","6","7","8","9","A","K","J","Q"]
signs=("rock","paper","scissor")
#num=random.randint(a,b)                 #int output

#num=random.random()                 #decimal random numbewr

"""
random.shuffle(cards) #['A', '7', '3', '1', '9', '8', '5', 'J', '2', '6', 'K', 'Q', '4']
print(cards)
"""

sign=random.choice(signs)
print(sign)