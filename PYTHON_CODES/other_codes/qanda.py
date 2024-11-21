##2d list
questions=["who is naruto",
           "what is luffy's father",
           "how many devil fruits does luffy eat"]
option=[["A.minato son","B.akatsuki mem","C.kakashi's son","D.sakura's bf"],
        ["A.garp","B.dragon","C.kaido","D.bigmom"],
        ["A.1","B.3","C.0","D.4"]]
answer=["A","B","A"]
user_ans=[]
ques_no=0
score=0
for question in questions:
    print("-----------------------------")
    print(question)
    for opt in option[ques_no]:
        print(opt)
    user_in=input("choose the option (A/B/C/D/):")
    user_ans.append(user_in.upper())
    if user_in.upper()==answer[ques_no]:
        print("correct answer")
        score+=1
    else:
        print("incorrect")
        print(f"correct answer is:{answer[ques_no]}")       
    ques_no+=1
print("your answers")
for i in user_ans:    
   print(i,end=" ")
print()
print("correct answers")
for j in answer:   
   print(j,end=" ")
print()    
result=(score/3)*100
print("---------------------")
print(f"YOU GOT :{result:.1f}%")
print("---------------------")
