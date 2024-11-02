import random
import string
char=" "+ string.punctuation +string.ascii_letters +string.digits
char=list(char)
#print(char)
encrpt_code=char.copy()
random.shuffle(encrpt_code)
#print(encrpt_code)

#encryption
org_text=input("enter the text to be encrypted: ")
encrypted=""
for _  in org_text:
    index=char.index(_)
    encrypted+=encrpt_code[index]
print(f" encryped text : {encrypted }")    

#decryption
encrypted_text=input("enter the text to decode : ")
orginal_text=""
for _ in encrypted_text:
    index=encrpt_code.index(_)
    orginal_text+=char[index]
print(f"decoded text : {orginal_text}")    