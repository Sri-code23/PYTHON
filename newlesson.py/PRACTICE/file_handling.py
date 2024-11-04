import json #json stands for java script object notation
import csv #csv stands for comma seperated values
import os 

#reading and writing text file
"""
try:
    
    
    with open("textfile.txt","x") as txt_file:
        txt_file.write("This is a new content")

    with open ("textfile.txt","r") as txt_file:
        operation=txt_file.read()
        print(operation)    

except Exception as e:
    print("Error reading file: ", e)

    """

#reading and writing json file
"""
try:
    with open("json_file.json","x") as json_file:
        if os.path.exists(json_file):
            print(f"{json_file} already exists ")
        else:    
            json.dump({"name":"John","age":30,"city":"New York"},json_file,indent=10)
            print(f"{json_file} is created")

    with open("json_file.json","r") as json_file:
        content=json.load(json_file)

except Exception as e:
    print("Error reading file: ", e )        
"""


#reading and writing csv file

try:
    csv_texts=[[1,2,3],[2,3,4],[3,4,5]]
    with open("csv_file.csv","x") as csv_file:
        location=csv.writer(csv_file)

        for row in csv_texts:
            location.writerow(row)
    
    with open("csv_file.csv","r") as csv_file:
        opened_file=csv.reader(csv_file)
        print(opened_file)

except Exception as a:
    print("Error writing file: ", a)
