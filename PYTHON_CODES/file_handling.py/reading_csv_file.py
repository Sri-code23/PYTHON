#readimg a csv file

import csv

file_path="csv_sample_file"
try:
    with open(file_path,"r") as file:
        content=csv.reader(file)
        for i in content:
            for row in i:
                print(row)
        print("done")
except FileExistsError as e:
    print("file alraedy exists" , e)

