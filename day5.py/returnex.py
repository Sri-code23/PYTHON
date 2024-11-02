def validate():
    username="sri"
    password=2312
    if (name==username) and (passw==password):
        return "login successful"
    else:
        return "username and password does not match"
name=input("enter your name:")
passw=int(input("enter your password:"))
validate()
print(validate())
 