#txt file

list1=["sri","dhar","anime","lol"]
content="sridhar loves watching anime"

file_name="C:\\Users\\vaath\\OneDrive\\Desktop/sri.txt"

#x-to create , w- to write , a-to add, r-to read

with open(file_name,"w") as file:   
    """
    file.write(content)
    print(f" {file_name} file is created")
""" 
    for word in list1:
        file.write(word + "\n")
    print(f" {file_name} list file is created")
        
        