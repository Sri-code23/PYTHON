#csv file - comma seperated values , used for excel & spreadsheets

import csv

content=[["name","age","dep"],
         ["sri",20,"ece"],
         ["dhar",23,"cse"]]

file_name="C:\\Users\\vaath\\OneDrive\\Desktop\\dharan.csv"

try:
    with open(file_name,"w") as file:
        locat=csv.writer(file) 
                    #location

        for row in content:
            locat.writerow(row)
        print("file created")

except Exception as e:
    print("file already exists", e)
