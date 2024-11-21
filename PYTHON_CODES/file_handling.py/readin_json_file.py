#reading json file
import json

file_path="new_sample.json"

with open(file_path,"r") as file:
    content=json.load(file)
    print(content)
