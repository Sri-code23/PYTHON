#counting the number divisible 3 and 5
three=0
five=0
for i in range (0,25):
    if(i%3==0):
        three+=1 #(three=three+1)==(three+=1)same meaning
    elif(i%5==0):
        five=five+1
print("nos divisible by 3:",three)
print("nos dividsible by 5:",five)