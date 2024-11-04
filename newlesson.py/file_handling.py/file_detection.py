import os

file1="advanced_python.txt/topics.txt"                    #filename

file2="newlesson.py/file_handling.py/sample_text.txt"     #dirctory/folder/file_name

file3="C:\\Users\\vaath\\OneDrive\\Desktop\\sampler.txt"                #loaction path , it is a folder in desktop

if os.path.exists(file3):
    print(f"'{file3}' does exists")
    if os.path.isfile(file3):      #if the file is a file it prints file
        print(" it is a file ")
    elif os.path.isdir(file3):     #if the file is a folder it prints directory
        print("it is a directory")
else:
    print(f" {file3} doesnot exists  !!!")


