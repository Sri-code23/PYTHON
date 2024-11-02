#print( "\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518") 
#● ┌ ─ ┐ │ └ ┘
import random
dice_dia={1:("┌───────┐",
             "│       │",
             "│   ●   │",
             "│       │",
             "└───────┘"),
          2:("┌───────┐",
             "│ ●     │",
             "│       │",
             "│     ● │",
             "└───────┘"),
          3:("┌───────┐",
             "│ ●     │",
             "│   ●   │",
             "│     ● │",
             "└───────┘"),
          4:("┌───────┐",
             "│ ●   ● │",
             "│       │",
             "│ ●   ● │",
             "└───────┘"),
          5:("┌───────┐",
             "│ ●   ● │",
             "│   ●   │",
             "│ ●   ● │",
             "└───────┘"),
          6:("┌───────┐",
             "│ ●   ● │",
             "│ ●   ● │",
             "│ ●   ● │",
             "└───────┘")}
dice=[]
total=0
user_inp=int(input("enter the number of times:"))
for i in range(1,user_inp+1):
  dice.append(random.randint(1,6))
print(dice)  
"""
for i in dice:
  for die in dice_dia.get(i):           #vertical
     print(die)
"""
for i in range(5):
  for die in dice:
    print(dice_dia.get(die)[i],end=" ")    # type: ignore       #horizontal
  print()



for i in dice:
  total=total+i
print(f"total:{total}")    


  