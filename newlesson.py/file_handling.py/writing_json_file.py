#json file is the collection key value pair

import json

content={"name":"sri","age":20,"desgn":"porgrammer"}
list1=["sri","dhar","anime","lol"]
file_name="sri_data.json"
try:   
    with open(file_name,"w") as file:
        json.dump(content,file,indent=4)
                  #what  #where

    with open(file_name,"a") as file:
        json.dump(list1,file,indent=5)
        print(f" {file_name} file has been created")

except FileExistsError:
    print("file already exists")