#dictionary
menu={"soda":30,
      "milk":25,
      "coffee":55,
      "tea":12}
cart=[]
total=0
print("-------MENU-------")
for item,value in menu.items():
    print(f"{item:10}:${value}")
while True:
    food=input("select the food item:")
    if food=="f":
      break
    elif menu.get(food) is not None:
       cart.append(food)
for i in cart:
  print(i,end=" ")
  total=total+ menu.get(i)
print()
print("-----------------")
print("----your bill----")
for food in cart:
   value=menu.get(food)
   print(f"{food:10}:{value:.2f}$")
print(f"total:{total:10,.2f}$")       
print("-----------------")
print("THANK YOU FOR PURCHASING")
