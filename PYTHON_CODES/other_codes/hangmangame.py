import random
words=["apple","orange","grapes","banana","mango","berry"]
hangman_art={0:("      ",
                "      ",
                "      "),
             1:("  o   ",
                "      ",
                "      "),
             2:("  o   ",
                "  |   ",
                "      "),
             3:("  o   ",
                " /|   ",
                "      "),
             4:("  o   ",
                " /|\\  ",
                "      "),
             5:("  o   ",
                " /|\\  ",
                " /    "),
             6:("  o   ",
                " /|\\",
                " / \\")}
def display_answer(answer):
    for letter in answer:
        print(letter,end=" ")
    print()
def display_hint(hint):
        print(" ".join(hint))

def display_man(wrong_guess):
    for i in hangman_art.get(wrong_guess):
        print(i)
    """    
    for j in range(3):
        for i in range(len(hangman_art)):
            print(hangman_art.get(i)[j], end=" ")
        print()
    """    



def main():
    wrong_guess=0
    condn=True
    answer=random.choice(words)
    hint=["_"]*len(answer)
    guessed_letters=set()

    while condn:
        display_man(wrong_guess)
        display_hint(hint)
        print()
        guess=input("enter your guess: ").lower()
        if not guess.isalpha() or len(guess)>1:
            print(" invalid input ")
            continue
    
        if guess in guessed_letters:
            print(f" letter {guess} already exists")
            continue
        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i]==guess:
                    hint[i]=guess

        else:
            print("wrong letter")  
            wrong_guess+=1    
        if "_" not in hint:
            display_answer(answer) 
            print("you win")      
        elif wrong_guess>=len(hangman_art)-1:
            display_answer(answer)
            print("you lose")
            break   


if __name__=="__main__":
    main()